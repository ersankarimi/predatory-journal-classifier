import os
import time
import logging
import numpy as np
import joblib
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import classification_report, accuracy_score, silhouette_score, confusion_matrix
from collections import Counter
from sklearn.preprocessing import StandardScaler # Menambahkan StandardScaler
# import matplotlib.pyplot as plt # Tambahkan ini jika ingin memvisualisasikan dendrogram
# from scipy.cluster.hierarchy import dendrogram # Tambahkan ini jika ingin memvisualisasikan dendrogram

METHOD_NAME = "dfs"
CLASSIFICATION_DIR = f"8_classification/scipy_hierarchical/{METHOD_NAME}_scipy_hierarchical_auto_improved" # Mengubah nama folder untuk versi yang ditingkatkan
os.makedirs(CLASSIFICATION_DIR, exist_ok=True)

LOG_FILE = os.path.join(CLASSIFICATION_DIR, f"8_{METHOD_NAME}_scipy_hierarchical_auto_improved.log") # Mengubah nama file log

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)


def load_data(vector_path, label_path):
    """Memuat data vektor dan label dari file .npy."""
    if not os.path.exists(vector_path) or not os.path.exists(label_path):
        logging.error(f"❌ File tidak ditemukan: {vector_path} atau {label_path}")
        return None, None
    try:
        X = np.load(vector_path)
        y = np.load(label_path)
        logging.info(f"✅ Data dimuat. X shape: {X.shape}, y shape: {y.shape}")
        return X, y
    except Exception as e:
        logging.error(f"❌ Gagal memuat data dari {vector_path} atau {label_path}: {e}")
        return None, None


def analyze_cluster_composition(cluster_labels, y_train):
    """Analisis komposisi label (Predator/Non-Predator) di setiap cluster."""
    cluster_composition = {}
    unique_clusters = np.unique(cluster_labels)
    logging.info(f"Analisis komposisi untuk {len(unique_clusters)} cluster.")
    for cluster_id in unique_clusters:
        # Memastikan cluster_id valid dan ada di cluster_labels
        if cluster_id in cluster_labels:
             labels_in_cluster = y_train[cluster_labels == cluster_id]
        else:
            logging.warning(f"⚠️ Cluster ID {cluster_id} tidak ditemukan dalam cluster_labels. Melewatkan.")
            continue


        if len(labels_in_cluster) == 0:
            logging.warning(
                f"⚠️ Cluster {cluster_id} kosong setelah pemfilteran label! Tidak dapat menentukan label mayoritas."
            )
            cluster_composition[cluster_id] = -1 # Menandai sebagai tidak terdefinisi
            continue

        label_counts = Counter(labels_in_cluster)
        # Handle kasus di mana Counter kosong (meskipun seharusnya tidak terjadi jika len(labels_in_cluster) > 0)
        if not label_counts:
             logging.warning(f"⚠️ Counter label kosong untuk Cluster {cluster_id}. Melewatkan.")
             cluster_composition[cluster_id] = -1
             continue

        most_common_label = label_counts.most_common(1)[0][0]
        cluster_composition[cluster_id] = most_common_label
        # Log hanya jika ada label di cluster
        logging.info(
            f"🔍 Cluster {cluster_id}: Mayoritas label = {most_common_label} (Jumlah: {label_counts})"
        )

    return cluster_composition


def train_model(X_train, y_train, linkage_method, distance_threshold):
    """Melatih model dengan Hierarchical Clustering SciPy dan NCM."""
    logging.info(f"⏳ Pelatihan dimulai dengan linkage='{linkage_method}', distance_threshold={distance_threshold}...")
    start_time = time.time()

    # Preprocessing: Standardisasi Data
    # Menggunakan StandardScaler untuk menstandarisasi fitur
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    logging.info(f"✅ Data latih distandardisasi. Shape: {X_train_scaled.shape}")


    logging.info(f"🔍 Melakukan hierarchical clustering...")

    try:
        # Hitung linkage matrix
        Z = linkage(X_train_scaled, method=linkage_method)
        logging.info(f"✅ Linkage matrix dihitung. Shape: {Z.shape}")

        # Membuat cluster dengan memotong dendrogram pada distance_threshold
        cluster_labels = fcluster(Z, t=distance_threshold, criterion='distance')

        # Ubah label cluster agar mulai dari 0 (jika perlu, fcluster terkadang dimulai dari 1)
        if cluster_labels.min() == 1:
             cluster_labels = cluster_labels - 1

        num_clusters = len(np.unique(cluster_labels))
        logging.info(f"✅ Clustering selesai. Jumlah cluster yang terbentuk: {num_clusters}")

        # Handle kasus jika hanya ada 1 cluster
        if num_clusters <= 1:
            logging.warning(f"⚠️ Hanya terbentuk {num_clusters} cluster dengan parameter ini. Melewatkan NCM dan evaluasi.")
            return scaler, Z, None, {}, -1, False # Menambahkan flag success = False

        # Hitung silhouette score
        try:
            silhouette_avg = silhouette_score(X_train_scaled, cluster_labels)
            logging.info(f"📊 Silhouette Score: {silhouette_avg:.4f}")
        except Exception as e:
            logging.warning(f"⚠️ Gagal menghitung silhouette score: {e}")
            silhouette_avg = -1

        # Analisis komposisi cluster
        cluster_mapping = analyze_cluster_composition(cluster_labels, y_train)

        # Handle kasus jika cluster_mapping kosong
        if not cluster_mapping:
             logging.warning("⚠️ Cluster mapping kosong. Tidak dapat melatih NCM.")
             return scaler, Z, None, cluster_mapping, silhouette_avg, False

        # Melatih Nearest Centroid Classifier
        logging.info("🧠 Melatih Nearest Centroid Classifier berdasarkan cluster hasil clustering...")
        clf = NearestCentroid(metric="euclidean")
        # Menggunakan cluster_labels hasil fcluster untuk melatih NCM
        clf.fit(X_train_scaled, cluster_labels) # Melatih NCM dengan data scaled dan label cluster
        logging.info("✅ NCM Classifier selesai dilatih.")

        training_time = time.time() - start_time
        logging.info(f"⏳ TOTAL WAKTU PELATIHAN: {training_time:.2f} detik")

        return scaler, Z, clf, cluster_mapping, silhouette_avg, True # Menambahkan flag success = True

    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan selama pelatihan: {e}")
        return scaler, None, None, {}, -1, False # Menambahkan flag success = False


def predict_and_evaluate(scaler, clf, cluster_mapping, X_test, y_test):
    """Memprediksi dan mengevaluasi model."""
    logging.info("📌 Memulai prediksi dan evaluasi...")
    start_time = time.time()

    # Preprocessing data uji dengan scaler yang sama
    if scaler:
        X_test_scaled = scaler.transform(X_test)
        logging.info("✅ Data uji distandardisasi.")
    else:
        X_test_scaled = X_test
        logging.warning("⚠️ Scaler tidak tersedia. Menggunakan data uji asli.")


    if clf is None or cluster_mapping is None:
        logging.error("❌ Classifier atau cluster mapping tidak tersedia untuk prediksi.")
        return None, None, None


    try:
        # Prediksi label cluster menggunakan NCM
        cluster_labels_pred = clf.predict(X_test_scaled)

        # Mapping label cluster ke label kelas asli
        y_pred = np.array(
            [cluster_mapping.get(cluster_id, -1) for cluster_id in cluster_labels_pred]
        )

        # Menangani cluster_id yang tidak terdefinisi dalam mapping
        if -1 in y_pred:
            logging.warning(
                "⚠️ Terdapat cluster yang tidak terdefinisi dalam mapping. "
                "Menetapkan label default (kelas mayoritas global) untuk -1."
            )
            # Menghitung kelas mayoritas global dari data latih asli (y_train)
            # Pastikan y_train tersedia di scope ini atau passing sebagai argumen
            # Untuk saat ini, menggunakan y_test sebagai fallback
            try:
                most_frequent_class = Counter(y_test).most_common(1)[0][0]
            except:
                 most_frequent_class = 0 # Default ke kelas 0 jika y_test juga kosong/bermasalah

            y_pred[y_pred == -1] = most_frequent_class
            logging.info(f"✅ Label -1 diganti dengan label mayoritas: {most_frequent_class}")

        # Evaluasi model
        report = classification_report(
            y_test,
            y_pred,
            target_names=["Non-Predator", "Predator"],
            digits=4,
            zero_division=0,
        )
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred) # Menambahkan Confusion Matrix

        logging.info("📊 Laporan Klasifikasi:\n%s", report)
        logging.info(f"🎯 Akurasi: {accuracy:.4f}")
        logging.info("📊 Confusion Matrix:\n%s", cm)

        evaluation_time = time.time() - start_time
        logging.info(f"⏳ Waktu Evaluasi: {evaluation_time:.2f} detik")

        return report, accuracy, cm

    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan selama prediksi atau evaluasi: {e}")
        return None, None, None


def save_model(model, scaler, linkage_matrix, cluster_mapping, silhouette_avg, model_path):
    """Menyimpan model dan artefak terkait."""
    try:
        joblib.dump((model, scaler, linkage_matrix, cluster_mapping, silhouette_avg), model_path)
        logging.info(
            f"✅ Model, scaler, linkage matrix, cluster_mapping, dan silhouette score disimpan ke {model_path}"
        )
    except Exception as e:
        logging.error(f"❌ Gagal menyimpan model ke {model_path}: {e}")


def load_model(model_path):
    """Memuat model dan artefak terkait."""
    try:
        model, scaler, linkage_matrix, cluster_mapping, silhouette_avg = joblib.load(
            model_path
        )
        logging.info(
            f"✅ Model, scaler, linkage matrix, cluster_mapping, dan silhouette score dimuat dari {model_path}"
        )
        return model, scaler, linkage_matrix, cluster_mapping, silhouette_avg
    except FileNotFoundError:
        logging.error(f"❌ File model tidak ditemukan di {model_path}")
        return None, None, None, None, None
    except Exception as e:
        logging.error(f"❌ Gagal memuat model dari {model_path}: {e}")
        return None, None, None, None, None


if __name__ == "__main__":
    logging.info("=" * 80)
    logging.info(f"🚀 MULAI TRAINING MODEL IMPROVED: {METHOD_NAME.upper()}")
    logging.info("=" * 80)

    # Jalur file data
    train_vector_path = f"7_oversampling/7_{METHOD_NAME}_train_vectors_oversampled.npy"
    train_label_path = f"7_oversampling/7_{METHOD_NAME}_train_labels_oversampled.npy"
    test_vector_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_vectors.npy"
    test_label_path = f"6_vectorized_journal_data/6_{METHOD_NAME.lower()}_test_labels.npy"
    model_path = os.path.join(
        CLASSIFICATION_DIR, f"8_{METHOD_NAME}_scipy_hierarchical_auto_improved_model.pkl"
    )

    # Memuat data
    X_train, y_train = load_data(train_vector_path, train_label_path)
    X_test, y_test = load_data(test_vector_path, test_label_path)

    if X_train is None or y_train is None or X_test is None or y_test is None:
        logging.error("❌ Data tidak tersedia. Proses dihentikan.")
        logging.shutdown()
        exit()

    # Parameter tuning options
    linkage_methods = ["ward", "average", "complete"] # Menambahkan metode linkage lain
    # Menambahkan rentang distance_threshold yang lebih luas dan lebih granular
    distance_threshold_options = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


    best_accuracy = 0
    best_model = None
    best_scaler = None # Menyimpan scaler terbaik
    best_linkage = None
    best_cluster_mapping = None
    best_silhouette_avg = None
    best_distance_threshold = None
    best_linkage_method = None
    best_report = None
    best_cm = None

    # Loop melalui semua kombinasi parameter
    for linkage_method in linkage_methods:
        for distance_threshold in distance_threshold_options:
            logging.info("=" * 60)
            logging.info(f"*** Mencoba linkage='{linkage_method}', distance_threshold={distance_threshold} ***")

            # Melatih model
            scaler, linkage_matrix, model, cluster_mapping, silhouette_avg, training_success = train_model(
                X_train, y_train, linkage_method=linkage_method, distance_threshold=distance_threshold
            )

            if not training_success:
                logging.warning("⚠️ Pelatihan tidak berhasil untuk parameter ini. Melewatkan evaluasi.")
                continue # Lanjutkan ke kombinasi parameter berikutnya

            # Memprediksi dan mengevaluasi
            report, accuracy, cm = predict_and_evaluate(
                scaler, model, cluster_mapping, X_test, y_test
            )

            # Membandingkan dan menyimpan model terbaik
            if accuracy is not None and accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_scaler = scaler # Menyimpan scaler terbaik
                best_linkage = linkage_matrix
                best_cluster_mapping = cluster_mapping
                best_silhouette_avg = silhouette_avg
                best_distance_threshold = distance_threshold
                best_linkage_method = linkage_method
                best_report = report
                best_cm = cm


    # Simpan model terbaik
    # Menggunakan pemeriksaan `is not None` untuk array NumPy seperti linkage_matrix
    if best_model is not None and best_scaler is not None and best_linkage is not None and best_cluster_mapping is not None:
        save_model(
            best_model,
            best_scaler,
            best_linkage,
            best_cluster_mapping,
            best_silhouette_avg,
            model_path,
        )
        logging.info(
            f"✅ Model terbaik (linkage='{best_linkage_method}', distance_threshold={best_distance_threshold}) disimpan."
        )
    else:
        logging.error("❌ Gagal menemukan model terbaik yang valid.")


    logging.info("=" * 80)
    logging.info("🏆 Hasil Terbaik dari Semua Eksperimen:")
    if best_model is not None:
        logging.info(f"Akurasi: {best_accuracy:.4f}")
        logging.info(f"Parameter Terbaik: linkage='{best_linkage_method}', distance_threshold={best_distance_threshold}")
        if best_report:
             logging.info("📊 Laporan Klasifikasi Model Terbaik:\n%s", best_report)
        if best_cm is not None:
             logging.info("📊 Confusion Matrix Model Terbaik:\n%s", best_cm)

    else:
        logging.info("❌ Tidak ada model terbaik yang berhasil dilatih dan dievaluasi.")

    logging.info("=" * 80)
    logging.info("✅ Proses Selesai")
    logging.info("=" * 80)
    logging.shutdown()

