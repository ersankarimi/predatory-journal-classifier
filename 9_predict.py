import requests
import logging
import joblib # Diubah dari pickle menjadi joblib
import numpy as np
from bs4 import BeautifulSoup
from gensim.models.doc2vec import Doc2Vec
from urllib.parse import urlparse
import random

# Misalnya NameFilter didefinisikan seperti ini saat menyimpan:
class NameFilter:
    def __init__(self, some_param=None):
        self.some_param = some_param
    def transform(self, x):
        return x

# Path model
DOC2VEC_MODEL_PATH = "6_vectorized_journal_data/6_doc2vec_dfs_train.model"
AUTOML_MODEL_PATH = "8_classification/dfs_90min/8_dfs_model.pkl"

# ===== User-Agent Pool (optional untuk menghindari blokir) =====
USER_AGENTS = [
    # Chrome - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",

    # Chrome - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",

    # Firefox - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",

    # Firefox - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:126.0) Gecko/20100101 Firefox/126.0",

    # Safari - macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",

    # Edge - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36 Edg/125.0.2535.67",

    # Android - Chrome
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Mobile Safari/537.36",

    # iPhone - Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Fungsi validasi URL format
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except:
        return False

# Fungsi scraping & ekstraksi struktur DOM dari <body>
def get_body_dom_structure(url):
    try:
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            raise ValueError(f"Status code {response.status_code} dari server.")
        soup = BeautifulSoup(response.text, "html.parser")
        body = soup.find("body")
        if body is None:
            raise ValueError("Tag <body> tidak ditemukan.")
        return extract_dom_structure(body)
    except Exception as e:
        logging.error(f"Gagal mengakses halaman: {e}")
        return None

# Fungsi rekursif DOM DFS
def extract_dom_structure(body):
    def recurse(element):
        return [{
            "tag": child.name,
            "children": recurse(child)
        } for child in element.find_all(recursive=False) if child.name]
    return recurse(body)

def extract_tags_dfs(dom):
    tags = []
    def dfs(node):
        if isinstance(node, list):
            for item in node:
                if item.get("tag"):
                    tags.append(item["tag"])
                if item.get("children"):
                    dfs(item["children"])
    dfs(dom)
    return tags

# Fungsi muat model
def load_models():
    logging.info("📥 Memuat model Doc2Vec dan AutoML...")
    doc2vec_model = Doc2Vec.load(DOC2VEC_MODEL_PATH)
    # Menggunakan joblib.load() karena model disimpan dengan joblib.dump()
    automl_model = joblib.load(AUTOML_MODEL_PATH)
    return doc2vec_model, automl_model

# Fungsi prediksi
def predict(url, doc2vec_model, automl_model):
    logging.info(f"🔗 Memproses tautan: {url}")
    dom = get_body_dom_structure(url)
    if dom is None:
        return None, "Gagal mengambil struktur DOM dari halaman."

    dfs_tags = extract_tags_dfs(dom)
    if not dfs_tags:
        return None, "DOM corpus kosong. Tidak dapat melakukan inferensi."

    # Periksa apakah model Doc2Vec mendukung infer_vector untuk list string
    # Gensim 4.x biasanya menerima list of strings
    vector = doc2vec_model.infer_vector(dfs_tags).reshape(1, -1)

    # autosklearn mengembalikan array numpy untuk predict dan predict_proba
    pred = automl_model.predict(vector)[0]
    prob = automl_model.predict_proba(vector)[0]
    confidence = max(prob)

    return (pred, confidence), None

# ===== Main Console App =====
if __name__ == "__main__":
    print("="*60)
    print("📊 Prediksi Kategori Jurnal: PREDATOR atau NON-PREDATOR")
    print("Masukkan tautan web jurnal yang ingin diuji.")
    print("="*60)

    try:
        doc2vec_model, automl_model = load_models()
    except Exception as e:
        logging.error(f"❌ Gagal memuat model: {e}")
        print(f"❌ Terjadi kesalahan fatal saat memuat model: {e}")
        print("Pastikan file model ada di lokasi yang benar dan tidak rusak.")
        exit()

    while True:
        url = input("\n🔗 Tautan jurnal (atau ketik 'exit' untuk keluar): ").strip()
        if url.lower() == "exit":
            print("👋 Keluar dari program.")
            break

        if not is_valid_url(url):
            print("⚠️ Format tautan tidak valid. Pastikan dimulai dengan http(s) dan domain benar.")
            continue

        result, error_msg = predict(url, doc2vec_model, automl_model)
        if error_msg:
            print(f"❌ {error_msg}")
            continue

        # autosklearn label 0 atau 1
        print(f"Result: {result}")
        label, confidence = result
        label_str = "PREDATOR" if label == 1 else "NON-PREDATOR"
        print(f"\n📌 Hasil Prediksi: {label_str}")
        print(f"   Keyakinan Model: {confidence:.2%}")
