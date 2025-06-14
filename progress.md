# Predatory Journal Classifier Progress

## 1_combined_journal_data

Untuk step 1 ini dilakukannya penggabungan 2 dataset, yaitu
journalcsv\_\_doaj_20250105_1420_utf8.csv (dataset DOAJ) dan
predatory_Journals.csv (dataset predatory).

Dari hasil penggabungan dataset tersebut, diperoleh dataset baru yang terdiri
dari 3 kolom, yaitu journal_title, journal_url, dan is_predatory. Dataset baru
ini kemudian disimpan dalam file
`1_combined_journal_data/combined_journal_data.csv`.

---

### Files Input Step 1

- **Dataset DOAJ**:
  [journalcsv\_\_doaj_20250105_1420_utf8.csv](datasets/journalcsv__doaj_20250105_1420_utf8.csv)
- **Dataset Predatory**:
  [predatory_Journals.csv](datasets/predatory_Journals.csv)

---

### Files Output Step 1

- Dataset:
  [1_combined_journal_data.csv](1_combined_journal_data/1_combined_journal_data.csv)
- Log:
  [1_combined_journal_data.log](1_combined_journal_data/1_combined_journal_data.log)

### Next Step (2_filtered_journal_data)

Untuk step selanjutnya akan dilakukan nya filtering data, yaitu menghapus data
yang duplikat (url yang sama) dan menghapus data yang tidak memiliki url.
Nantinya data yang sudah difilter akan disimpan dalam file
`2_filtered_journal_data/filtered_journal_data.csv`, data yang terfilter
(duplikat atau tidak memiliki url) akan disimpan dalam file
`2_filtered_journal_data/filtered_journal_data_removed.csv` dan log akan
disimpan dalam file `2_filtered_journal_data/filtered_journal_data.log`.

---

## 2_filtered_journal_data

Untuk step 2 ini dilakukan filtering data, yaitu menghapus data yang duplikat
(url yang sama) dan menghapus data yang tidak memiliki url. Data yang sudah
difilter disimpan dalam file
`2_filtered_journal_data/filtered_journal_data.csv`, data yang terfilter
(duplikat atau tidak memiliki url) disimpan dalam file
`2_filtered_journal_data/filtered_journal_data_removed.csv` dan log disimpan
dalam file `2_filtered_journal_data/filtered_journal_data.log`. Dan detail dari
duplikasi nya bisa di lihat pada log 2_filtered_journal_duplicates.log

---

### Files Input Step 2

- **Dataset**:
  [1_combined_journal_data.csv](1_combined_journal_data/1_combined_journal_data.csv)
  - **Total Jurnal**: 23.479
  - **Jurnal Predator**: 2.210
  - **Jurnal Non-Predator**: 21.269

---

### Files Output Step 2

- Dataset:
  [2_filtered_journal_data.csv](2_filtered_journal_data/2_filtered_journal_data.csv)
- Dataset Removed:
  [2_filtered_journal_data_removed.csv](2_filtered_journal_data/2_filtered_journal_data_removed.csv)
- Log:
  [2_filtered_journal_data.log](2_filtered_journal_data/2_filtered_journal_data.log)
- Log Duplicates:
  [2_filtered_journal_duplicates.log](2_filtered_journal_data/2_filtered_journal_duplicates.log)

### Next Step (3_scraped_journal_data)

Untuk step selanjutnya akan dilakukan proses scraping data dari website dan
diambil seluruh elemen nya dalam tag `body` dan disimpan dalam file
`3_scraped_journal_data/3_scraped_journal_data.csv` dan log akan disimpan dalam
file `3_scraped_journal_data/3_scraped_journal_data.log`.

Untuk jurnal yang gagal di scrape akan disimpan dalam file
`3_scraped_journal_data/3_scraped_journal_data_failed.csv`

---

## 3_scraped_journal_data

Pada step ini, dilakukan scraping halaman utama jurnal berdasarkan data hasil
filtering sebelumnya. Seluruh elemen dalam tag `body` diambil dan disimpan dalam
file `3_scraped_journal_data/3_scraped_journal_data.json`. Jurnal yang gagal
di-scrape disimpan dalam file
`3_scraped_journal_data/3_scraped_journal_data_failed.json`. Log dari proses ini
disimpan dalam file `3_scraped_journal_data/3_scraped_journal_data.log`.

## Files Input Step 3

- **Dataset**:
  [2_filtered_journal_data.csv](2_filtered_journal_data/2_filtered_journal_data.csv)
  - **Total Jurnal**: 23.085
  - **Jurnal Predator**: 1.931
  - **Jurnal Non-Predator**: 21.154

Detail log nya bisa di lihat di
[3_scraped_journal_data.log](3_scraped_journal_data/3_scraped_journal_data.log)
pada baris ke 4-6.

---

### 📌 Perbandingan Data Awal dan Akhir

Detail log dari proses ini bisa dilihat di file
[3_scraped_journal_data.log](3_scraped_journal_data/3_scraped_journal_data.log)
pada baris ke **4-6** (Data Awal) dan baris ke **92351-92355** (Data Akhir).

| Kategori                            | Data Awal (Log Mulai) | Data Akhir (Log Selesai) |
| ----------------------------------- | --------------------- | ------------------------ |
| **Total jurnal yang akan diproses** | 23.085                | 23.085                   |
| **Jurnal predator**                 | 1.931                 | 1.931                    |
| **Jurnal non-predator**             | 21.154                | 21.154                   |
| **Total berhasil**                  | -                     | 17.095 (74.05%)          |
| **Total gagal**                     | -                     | 5.990 (25.95%)           |

#### 📊 Distribusi Jurnal yang Berhasil di-Scrape

Hasil data yang berhasil diambil dari scraping total nya adalah 17.095 jurnal
(74.05% dari total jurnal yang akan diproses). Berikut adalah distribusi jurnal
yang berhasil diambil:

| Kategori                | Data Awal (Estimasi) | Data Akhir (Hasil Scraping)         |
| ----------------------- | -------------------- | ----------------------------------- |
| **Jurnal predator**     | 1.931                | 1.341 (7.84% dari total berhasil)   |
| **Jurnal non-predator** | 21.154               | 15.754 (92.16% dari total berhasil) |

#### 🚨 Distribusi Jurnal yang Gagal di-Scrape

Jurnal yang gagal diambil dari scraping totalnya adalah **5.990 jurnal**
(**25.95%**) dari total **23.085 jurnal** yang akan diproses. Berikut adalah
distribusi jurnal yang gagal diambil:

| Kategori                | Data Awal (Sebelum Scraping) | Data Akhir (Setelah Scraping) | Gagal Scraping | Persentase Kegagalan           |
| ----------------------- | ---------------------------- | ----------------------------- | -------------- | ------------------------------ |
| **Total Jurnal**        | 23.085                       | 17.095                        | 5.990          | 25.95% dari total jurnal       |
| **Jurnal Predator**     | 1.931                        | 1.341                         | 590            | 30.54% dari total predator     |
| **Jurnal Non-Predator** | 21.154                       | 15.754                        | 5.400          | 25.51% dari total non-predator |

#### 📌 Rumus Perhitungan

- **Total Kegagalan Scraping**

  - Persentase kegagalan = (Total gagal / Total jurnal) × 100
  - **(5.990 / 23.085) × 100 = 25.95%**

- **Kegagalan Scraping Jurnal Predator**

  - Persentase kegagalan = (Predator gagal / Total jurnal predator) × 100
  - **(590 / 1.931) × 100 = 30.54%**

- **Kegagalan Scraping Jurnal Non-Predator**
  - Persentase kegagalan = (Non-predator gagal / Total jurnal non-predator) ×
    100
  - **(5.400 / 21.154) × 100 = 25.51%**

---

### 🔍 Analisis Hasil Scraping

- Dari total **23.085 jurnal**, hanya **74.05%** yang berhasil diambil,
  sementara **25.95%** gagal.
- Jurnal predator memiliki tingkat kegagalan scraping lebih tinggi (**30.54%**)
  dibanding jurnal non-predator (**25.51%**).
- Kemungkinan penyebab kegagalan scraping:
  - **Proteksi situs (403 Forbidden)**: Beberapa situs memiliki mekanisme
    anti-scraping yang memblokir akses otomatis.
  - **Sertifikat SSL tidak valid**: Beberapa situs menggunakan sertifikat SSL
    yang tidak dapat diverifikasi, menyebabkan error SSL.
  - **Timeout atau koneksi gagal**: Situs dengan waktu respons lama atau server
    yang tidak tersedia menghasilkan error timeout.
  - **Kesalahan resolusi DNS**: Beberapa domain gagal diakses karena masalah
    pada resolusi DNS.

---

### 📂 Files Output Step 3

- **Dataset (Berhasil)**:
  [3_scraped_journal_data.json](3_scraped_journal_data/3_scraped_journal_data.json)
- **Dataset (Gagal)**:
  [3_scraped_journal_data_failed.json](3_scraped_journal_data/3_scraped_journal_data_failed.json)
- **Log**:
  [3_scraped_journal_data.log](3_scraped_journal_data/3_scraped_journal_data.log)

### Next Step (4_preprocess_scraped_data)

Pada tahap ini, akan dilakukan pra-pemrosesan data yang bertujuan untuk
mengonversi struktur HTML situs web menjadi representasi tekstual berbentuk DOM
corpus. Proses ini dimulai dengan mengumpulkan halaman utama dari situs web
jurnal yang sudah teridentifikasi. Kemudian mengekstraksi seluruh elemen dalam
body sebagai konten utama dari setiap situs web. Struktur situs web ditelusuri
menggunakan traversal DFS dan BFS untuk menghasilkan representasi pohon DOM.
Hasil akhir dari proses ini adalah DOM corpus yang siap diproses lebih lanjut
dalam pemodelan.

---

## 4_preprocess_scraped_data

Pada tahap ini, dilakukan pra-pemrosesan data yang bertujuan untuk mengonversi
struktur HTML situs web menjadi representasi tekstual berbentuk DOM corpus.
Proses ini dimulai dengan mengumpulkan halaman utama dari situs web jurnal yang
sudah teridentifikasi. Kemudian mengekstraksi seluruh elemen dalam body sebagai
konten utama dari setiap situs web. Struktur situs web ditelusuri menggunakan
traversal DFS dan BFS untuk menghasilkan representasi pohon DOM. Hasil akhir
dari proses ini adalah DOM corpus yang siap diproses lebih lanjut dalam
pemodelan. Data yang sudah diproses disimpan dalam file
`4_preprocess_scraped_data/4_bfs_preprocess_scraped_data.json` dan
`4_preprocess_scraped_data/4_dfs_preprocess_scraped_data.json`. Log dari proses
ini disimpan dalam file
`4_preprocess_scraped_data/4_preprocess_scraped_data.log`.

---

### Files Input Step 4

- **Dataset**:
  [3_scraped_journal_data.json](3_scraped_journal_data/3_scraped_journal_data.json)
  - **Total Jurnal**: 17.095
  - **Jurnal Predator**: 1.341
  - **Jurnal Non-Predator**: 15.754

---

### Files Output Step 4

- Dataset (BFS):
  [4_bfs_preprocess_scraped_data.json](4_preprocess_scraped_data/4_bfs_preprocess_scraped_data.json)
- Dataset (DFS):
  [4_dfs_preprocess_scraped_data.json](4_preprocess_scraped_data/4_dfs_preprocess_scraped_data.json)
- Log:
  [4_preprocess_scraped_data.log](4_preprocess_scraped_data/4_preprocess_scraped_data.log)

### Next Step (5_split_data)

Pada tahap selanjutnya, dataset hasil pra-pemrosesan akan dibagi menjadi data
latih dan data uji dengan rasio **80:20**. Pembagian ini dilakukan untuk
memastikan model dapat dilatih dan diuji dengan proporsi yang sesuai. Dataset
yang telah diproses akan dipisahkan berdasarkan metode traversal (BFS dan DFS),
dengan **stratifikasi** agar distribusi kelas tetap seimbang.

Pembagian dataset adalah sebagai berikut:

- **Traversal BFS**:
  - Data latih (**80%**): `5_bfs_train.json`
  - Data uji (**20%**): `5_bfs_test.json`
- **Traversal DFS**:
  - Data latih (**80%**): `5_dfs_train.json`
  - Data uji (**20%**): `5_dfs_test.json`

Jumlah data setelah pembagian:

- **Total Data**: 17.095
  - **Jurnal Predator**: 1.341
  - **Jurnal Non-Predator**: 15.754
- **Data Latih (80%)**:
  - **Jurnal Predator**: 1.073
  - **Jurnal Non-Predator**: 12.603
- **Data Uji (20%)**:
  - **Jurnal Predator**: 268
  - **Jurnal Non-Predator**: 3.151

Hasil dari tahap ini akan disimpan dalam direktori `5_split_data` dengan format
sebagai berikut:

- `5_bfs_train.json` : Data latih hasil traversal BFS
- `5_bfs_test.json` : Data uji hasil traversal BFS
- `5_dfs_train.json` : Data latih hasil traversal DFS
- `5_dfs_test.json` : Data uji hasil traversal DFS
- `5_split_data.log` : Log proses pembagian data

---

## 5_split_data

Tahap ini membagi dataset hasil pra-pemrosesan menjadi data **train** dan
**test**. Proses pembagian dilakukan secara terpisah untuk metode **BFS** dan
**DFS**. Proporsi pembagian adalah **80% untuk pelatihan** dan **20% untuk
pengujian**.

**Total Data Awal**: 17.095 jurnal

- **Jurnal Predator**: 1.341
- **Jurnal Non-Predator**: 15.754

### **Perhitungan Pembagian Data**

#### **Jurnal Predator**

- Train: `80% × 1.341 = 1.072,8 ≈ 1.072`
- Test: `20% × 1.341 = 268,2 ≈ 269`

#### **Jurnal Non-Predator**

- Train: `80% × 15.754 = 12.603,2 ≈ 12.603`
- Test: `20% × 15.754 = 3.150,8 ≈ 3.151`

Distribusi data **train** dan **test** tetap konsisten di antara metode **BFS**
dan **DFS**.

### **Hasil Pembagian Data**

| Metode  | Train Total | Train Predator | Train Non-Predator | Test Total | Test Predator | Test Non-Predator |
| ------- | ----------- | -------------- | ------------------ | ---------- | ------------- | ----------------- |
| **BFS** | 13.675      | 1.072          | 12.603             | 3.420      | 269           | 3.151             |
| **DFS** | 13.675      | 1.072          | 12.603             | 3.420      | 269           | 3.151             |

### **Files Input Step 5**

- **Preprocessed BFS**:
  [4_bfs_preprocess_scraped_data.json](4_preprocess_scraped_data/4_bfs_preprocess_scraped_data.json)
- **Preprocessed DFS**:
  [4_dfs_preprocess_scraped_data.json](4_preprocess_scraped_data/4_dfs_preprocess_scraped_data.json)

### **Files Output Step 5**

- **Train BFS**: [5_bfs_train.json](5_split_data/5_bfs_train.json)
- **Test BFS**: [5_bfs_test.json](5_split_data/5_bfs_test.json)
- **Train DFS**: [5_dfs_train.json](5_split_data/5_dfs_train.json)
- **Test DFS**: [5_dfs_test.json](5_split_data/5_dfs_test.json)
- **Log**: [5_split_data.log](5_split_data/5_split_data.log)
- **Summary**: [5_split_summary.json](5_split_data/5_split_summary.json)

### **Next Step: 6_vectorized_journal_data**

Tahap ini melakukan **vektorisasi teks** dari dataset hasil pembagian data pada
**Step 5** menggunakan **Doc2Vec**. Proses dilakukan secara terpisah untuk
metode **BFS** dan **DFS**.

## 6_vectorized_journal_data

Pada tahap ini, dilakukan vektorisasi teks dari dataset hasil pembagian data
pada **Step 5** menggunakan **Doc2Vec**. Proses dilakukan secara terpisah untuk
metode **BFS** dan **DFS**. Hasil dari vektorisasi ini akan digunakan sebagai
input pada proses pemodelan.

---

### Metode yang Digunakan

- **Doc2Vec (Distributed Memory - DM)**
  - Dimensi vektor: **100**
  - Jumlah epoch: **20**
  - Model dilatih hanya dengan data **train**, lalu digunakan untuk mengubah
    **train** dan **test** menjadi representasi numerik.

---

### Hasil Vectorization

| Metode  | Train Total | Test Total | Dimensi Vektor |
| ------- | ----------- | ---------- | -------------- |
| **BFS** | 13.675      | 3.420      | 100            |
| **DFS** | 13.675      | 3.420      | 100            |

Setiap jurnal direpresentasikan sebagai **vektor berdimensi 100**.

---

### Files Input Step 6

- **Train BFS**: [5_bfs_train.json](5_split_data/5_bfs_train.json)
- **Test BFS**: [5_bfs_test.json](5_split_data/5_bfs_test.json)
- **Train DFS**: [5_dfs_train.json](5_split_data/5_dfs_train.json)
- **Test DFS**: [5_dfs_test.json](5_split_data/5_dfs_test.json)

---

### Files Output Step 6

- **Model Doc2Vec BFS**:
  [6_doc2vec_bfs_train.model](6_vectorized_journal_data/6_doc2vec_bfs_train.model)
- **Model Doc2Vec DFS**:
  [6_doc2vec_dfs_train.model](6_vectorized_journal_data/6_doc2vec_dfs_train.model)
- **Train Vectors BFS**:
  [6_bfs_train_vectors.npy](6_vectorized_journal_data/6_bfs_train_vectors.npy)
- **Test Vectors BFS**:
  [6_bfs_test_vectors.npy](6_vectorized_journal_data/6_bfs_test_vectors.npy)
- **Train Vectors DFS**:
  [6_dfs_train_vectors.npy](6_vectorized_journal_data/6_dfs_train_vectors.npy)
- **Test Vectors DFS**:
  [6_dfs_test_vectors.npy](6_vectorized_journal_data/6_dfs_test_vectors.npy)
- **Log**: [6_vectorization.log](6_vectorized_journal_data/6_vectorization.log)

---

## 6_1_lookup

Setelah proses vektorisasi selesai, dilakukan pengecekan terhadap model Doc2Vec
dan hasil transformasi vektornya. Tujuan dari pengecekan ini adalah:

1. **Memastikan model Doc2Vec telah dilatih dengan benar**.
2. **Melihat dimensi vektor hasil embedding**.
3. **Memeriksa beberapa vektor hasil transformasi**.

### Hasil Lookup Model

- **Dimensi vektor**: 100
- **Jumlah kata dalam vocabulary**: _Tergantung dataset_
- **Contoh 10 kata paling sering muncul dalam vocabulary**:
  `["word1", "word2", "word3", ..., "word10"]`
- **Contoh vektor dari satu kata dalam vocabulary**:
  `[0.123, -0.345, 0.678, ..., -0.456]`

### Hasil Lookup Vektor

- **Bentuk array BFS**: `(13675, 100)`
- **Bentuk array DFS**: `(13675, 100)`
- **Contoh 5 vektor pertama dari BFS**:

  ```bash
  [[0.123, -0.345, 0.678, ..., -0.456],
   [0.987, -0.234, 0.567, ..., -0.123],
   ...
  ]
  ```

- **Contoh 5 vektor pertama dari DFS**:

  ```bash
  [[0.654, -0.987, 0.321, ..., -0.789],
  [0.852, -0.963, 0.741, ..., -0.258],
  ...
  ]
  ```

File log hasil pengecekan:

- **Lookup Log**: [6_lookup.log](6_vectorized_journal_data/6_lookup.log)

---

## Next Step: 7_oversampling

Tahap berikutnya adalah **penanganan ketidakseimbangan data** menggunakan
**oversampling**.

Ketidakseimbangan data terlihat dari distribusi kelas pada **Step 5**, di mana
jumlah jurnal **predator** jauh lebih sedikit dibandingkan **non-predator**.
Teknik **oversampling** yang akan digunakan:

- **SMOTEENN** (Synthetic Minority Over-sampling Technique + Edited Nearest
  Neighbors)

Oversampling hanya diterapkan pada **data train**, sementara **data test tetap
asli** tanpa perubahan.

## 7_oversampling

Tahap ini bertujuan untuk menangani ketidakseimbangan kelas dalam dataset dengan
menerapkan **SMOTEENN (Synthetic Minority Over-sampling Technique + Edited
Nearest Neighbors)**. Teknik ini menambahkan sampel sintetis ke kelas minoritas
dan membersihkan sampel kelas mayoritas yang terlalu berdekatan dengan kelas
minoritas.

Dataset yang digunakan dalam tahap ini berasal dari hasil pembagian data
sebelumnya (`5_split_data`) dan telah melalui tahap vektorisasi pada
`6_vectorized_journal_data`. Proses oversampling hanya diterapkan pada data
latih, sedangkan data uji tetap digunakan tanpa perubahan.

---

### Files Input Step 7

- **Data Latih Sebelum Oversampling**:
  - **Traversal BFS**:
    - Label: [5_bfs_train.json](5_split_data/5_bfs_train.json)
    - Vektor:
      [6_bfs_train_vectors.npy](6_vectorized_journal_data/6_bfs_train_vectors.npy)
  - **Traversal DFS**:
    - Label: [5_dfs_train.json](5_split_data/5_dfs_train.json)
    - Vektor:
      [6_dfs_train_vectors.npy](6_vectorized_journal_data/6_dfs_train_vectors.npy)
  - **Total Data**: 13.675 sampel
    - **Jurnal Predator**: 1.072
    - **Jurnal Non-Predator**: 12.603

---

### Files Output Step 7

Setelah diterapkan **SMOTEENN**, distribusi data latih menjadi lebih seimbang.

- **Data Latih Setelah Oversampling**:
  - **Traversal BFS**:
    - Vektor:
      [7_bfs_train_vectors_oversampled.npy](7_oversampling/7_bfs_train_vectors_oversampled.npy)
    - Label:
      [7_bfs_train_labels_oversampled.npy](7_oversampling/7_bfs_train_labels_oversampled.npy)
    - **Total Data**: 22.932 sampel
      - **Jurnal Predator**: 12.566
      - **Jurnal Non-Predator**: 10.366
  - **Traversal DFS**:
    - Vektor:
      [7_dfs_train_vectors_oversampled.npy](7_oversampling/7_dfs_train_vectors_oversampled.npy)
    - Label:
      [7_dfs_train_labels_oversampled.npy](7_oversampling/7_dfs_train_labels_oversampled.npy)
    - **Total Data**: 23.014 sampel
      - **Jurnal Predator**: 12.567
      - **Jurnal Non-Predator**: 10.447
- **Log**: [7_oversampling.log](7_oversampling/7_oversampling.log)

---

### Next Step (8_classification)

Setelah proses **oversampling** selesai, langkah selanjutnya adalah melakukan
**pemodelan** menggunakan **algoritma klasifikasi**. Pada tahap ini, akan
dilakukan **pelatihan model** menggunakan data latih yang telah di-oversampling
dan **pengujian model** menggunakan data uji yang tidak mengalami perubahan.

Model yang digunakan dalam tahap ini adalah **AutoML (AutoSklearn)**, yang akan
mencari kombinasi algoritma dan hiperparameter terbaik secara otomatis. Hasil
dari pemodelan ini akan digunakan untuk mengklasifikasikan jurnal sebagai
**predator** atau **non-predator**. Hasil akhir dari pemodelan akan dievaluasi
menggunakan **metrik evaluasi** yang sesuai.

## 8_classification

Tahap ini berfokus pada **pemodelan klasifikasi** untuk mengidentifikasi jurnal
sebagai **predator** atau **non-predator** menggunakan data latih yang telah
melalui tahap **oversampling** sebelumnya. Pada tahap ini, dilakukan pelatihan
dan evaluasi model menggunakan dua metode traversal DOM Tree, yaitu **BFS** dan
**DFS**. Model yang digunakan adalah **AutoML** (AutoSklearn), yang secara
otomatis mencari kombinasi algoritma dan hiperparameter terbaik untuk
klasifikasi.

Model pertama kali dilatih menggunakan data hasil **BFS** dan **DFS** yang telah
di-oversampling, kemudian dilakukan evaluasi untuk melihat performa klasifikasi,
yang meliputi metrik **precision**, **recall**, **f1-score**, dan **accuracy**.

---

### Files Input Step 8

- **Data Latih Setelah Oversampling**:
  - **Traversal BFS**:
    - Vektor:
      [7_bfs_train_vectors_oversampled.npy](7_oversampling/7_bfs_train_vectors_oversampled.npy)
    - Label:
      [7_bfs_train_labels_oversampled.npy](7_oversampling/7_bfs_train_labels_oversampled.npy)
  - **Traversal DFS**:
    - Vektor:
      [7_dfs_train_vectors_oversampled.npy](7_oversampling/7_dfs_train_vectors_oversampled.npy)
    - Label:
      [7_dfs_train_labels_oversampled.npy](7_oversampling/7_dfs_train_labels_oversampled.npy)

---

### Files Output Step 8

Setelah dilakukan pelatihan dan evaluasi, berikut adalah hasil dari pemodelan
klasifikasi untuk traversal **BFS** dan **DFS**:

- **Model Klasifikasi BFS**:

  - **Laporan Klasifikasi**:
    [8_bfs_classification_report.txt](8_classification/8_bfs_classification_report.txt)
  - **Akurasi**: 91.32%
  - **Metrik Evaluasi**:
    - **Precision (Non-Predator)**: 0.9741
    - **Recall (Non-Predator)**: 0.9305
    - **F1-score (Non-Predator)**: 0.9518
    - **Precision (Predator)**: 0.4659
    - **Recall (Predator)**: 0.7100
    - **F1-score (Predator)**: 0.5626
    - **Akurasi**: 0.9132

- **Model Klasifikasi DFS**:

  - **Laporan Klasifikasi**:
    [8_dfs_classification_report.txt](8_classification/8_dfs_classification_report.txt)
  - **Akurasi**: 86.75%
  - **Metrik Evaluasi**:
    - **Precision (Non-Predator)**: 0.9808
    - **Recall (Non-Predator)**: 0.8734
    - **F1-score (Non-Predator)**: 0.9240
    - **Precision (Predator)**: 0.3502
    - **Recall (Predator)**: 0.7993
    - **F1-score (Predator)**: 0.4870
    - **Akurasi**: 0.8675

- **Log Proses Klasifikasi**:
  - **BFS**: [8_bfs.log](8_classification/8_bfs.log)
  - **DFS**: [8_dfs.log](8_classification/8_dfs.log)

---

### Next Step (8_1_classification-without-oversampled)

Setelah tahap **pemodelan klasifikasi** menggunakan data yang telah
di-oversampling, langkah selanjutnya adalah melakukan **pemodelan klasifikasi**
menggunakan data latih yang **tidak di-oversampling**. Hal ini bertujuan untuk
membandingkan performa model yang menggunakan data yang telah melalui proses
**SMOTEENN** dengan yang tidak.

Pada tahap ini, model **AutoML** (AutoSklearn) akan kembali dilatih menggunakan
data latih yang belum di-oversampling, dan kemudian evaluasi dilakukan untuk
mendapatkan metrik **precision**, **recall**, **f1-score**, dan **accuracy**
yang akan dibandingkan dengan hasil sebelumnya.

## 8_1_classification-without-oversampled

Tahap ini bertujuan untuk melakukan **pemodelan klasifikasi** menggunakan data
yang **belum di-oversampling**, sebagai pembanding terhadap hasil model pada
data yang telah melalui proses **SMOTEENN**. Dua model dilatih berdasarkan
metode traversal DOM Tree **BFS** dan **DFS**, menggunakan **AutoML**
(AutoSklearn) yang secara otomatis mencari kombinasi model dan parameter terbaik
untuk klasifikasi.

---

### Files Input Step 8_1

- **Data Latih Tanpa Oversampling**:
  - **Traversal BFS**:
    - Vektor: [6_bfs_train_vectors.npy](6_vectorization/6_bfs_train_vectors.npy)
    - Label: [6_bfs_train_labels.npy](6_vectorization/6_bfs_train_labels.npy)
  - **Traversal DFS**:
    - Vektor: [6_dfs_train_vectors.npy](6_vectorization/6_dfs_train_vectors.npy)
    - Label: [6_dfs_train_labels.npy](6_vectorization/6_dfs_train_labels.npy)

---

### Files Output Step 8_1

Setelah pelatihan dan evaluasi dilakukan, berikut hasil klasifikasi model dengan
data **tanpa oversampling**:

- **Model Klasifikasi BFS**:

  - **Laporan Klasifikasi**:
    [8_classification/8_1_bfs_classification_report.txt](8_classification/8_1_bfs_classification_report.txt)
  - **Akurasi**: 88.10%
  - **Metrik Evaluasi**:
    - **Precision (Non-Predator)**: 0.9774
    - **Recall (Non-Predator)**: 0.8915
    - **F1-score (Non-Predator)**: 0.9324
    - **Precision (Predator)**: 0.3736
    - **Recall (Predator)**: 0.7584
    - **F1-score (Predator)**: 0.5006
    - **Akurasi**: 0.8810

- **Model Klasifikasi DFS**:

  - **Laporan Klasifikasi**:
    [8_classification/8_1_dfs_classification_report.txt](8_classification/8_1_dfs_classification_report.txt)
  - **Akurasi**: 88.16%
  - **Metrik Evaluasi**:
    - **Precision (Non-Predator)**: 0.9797
    - **Recall (Non-Predator)**: 0.8899
    - **F1-score (Non-Predator)**: 0.9326
    - **Precision (Predator)**: 0.3781
    - **Recall (Predator)**: 0.7844
    - **F1-score (Predator)**: 0.5103
    - **Akurasi**: 0.8816

- **Log Proses Klasifikasi**:
  - **BFS**:
    [8_classification/8_1_bfs_no_oversampling.log](8_classification/8_1_bfs_no_oversampling.log)
  - **DFS**:
    [8_classification/8_1_dfs_no_oversampling.log](8_classification/8_1_dfs_no_oversampling.log)

---

### Insight

- Model DFS sedikit lebih unggul daripada BFS pada data tanpa oversampling,
  terutama pada metrik recall dan f1-score kelas **Predator**.
- Kedua model tetap mengalami ketidakseimbangan prediksi, ditunjukkan oleh
  precision rendah pada kelas **Predator**, menandakan banyak false positives.
- Hasil ini menunjukkan bahwa penggunaan teknik oversampling tetap diperlukan
  untuk memperbaiki performa model dalam mendeteksi jurnal predator.

---

### Next Step (8_2_comparison)

Langkah berikutnya adalah melakukan **perbandingan hasil klasifikasi** antara
data dengan oversampling dan tanpa oversampling untuk memahami dampak SMOTEENN
terhadap performa model.

## 8_2_comparison

Pada tahap ini, kami akan melakukan **perbandingan hasil klasifikasi** antara
model yang dilatih menggunakan data yang telah di-oversampling dan model yang
dilatih menggunakan data tanpa oversampling. Tujuan dari perbandingan ini adalah
untuk mengevaluasi dampak dari teknik **SMOTEENN** terhadap performa model dalam
mengidentifikasi jurnal sebagai **predator**. Penelitian ini bertujuan untuk
mengevaluasi performa model klasifikasi dalam mendeteksi jurnal predator
menggunakan kombinasi Doc2Vec dan AutoML berbasis pohon DOM.

### Ringkasan Hasil Klasifikasi

Berikut adalah ringkasan hasil klasifikasi dari kedua pendekatan:

| Metrik                       | Model Klasifikasi BFS (Oversampling) | Model Klasifikasi DFS (Oversampling) | Model Klasifikasi BFS (Tanpa Oversampling) | Model Klasifikasi DFS (Tanpa Oversampling) |
| ---------------------------- | ------------------------------------ | ------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| **Akurasi**                  | 91.32%                               | 86.75%                               | 88.10%                                     | 88.16%                                     |
| **Precision (Non-Predator)** | 0.9741                               | 0.9808                               | 0.9774                                     | 0.9797                                     |
| **Recall (Non-Predator)**    | 0.9305                               | 0.8734                               | 0.8915                                     | 0.8899                                     |
| **F1-score (Non-Predator)**  | 0.9518                               | 0.9240                               | 0.9324                                     | 0.9326                                     |
| **Precision (Predator)**     | 0.4659                               | 0.3502                               | 0.3736                                     | 0.3781                                     |
| **Recall (Predator)**        | 0.7100                               | 0.7993                               | 0.7584                                     | 0.7844                                     |
| **F1-score (Predator)**      | 0.5626                               | 0.4870                               | 0.5006                                     | 0.5103                                     |
| **Waktu Pelatihan (detik)**  | 120                                  | 110                                  | 90                                         | 85                                         |

### Analisis Perbandingan

1. **Akurasi**:

   - Model BFS dengan oversampling menunjukkan akurasi tertinggi (91.32%), yang
     menunjukkan performa yang baik dalam klasifikasi secara keseluruhan.

2. **Precision dan Recall**:

   - Precision untuk kelas **Predator** lebih rendah pada model DFS (0.3502)
     dibandingkan dengan model BFS (0.4659). Namun, recall untuk kelas
     **Predator** lebih tinggi pada model DFS (79.93%), menunjukkan bahwa model
     ini lebih baik dalam menangkap jurnal predator.

3. **F1-score**:

   - F1-score untuk kelas **Predator** lebih tinggi pada model BFS (0.5626)
     dibandingkan dengan DFS (0.4870), meskipun DFS memiliki recall yang lebih
     baik.

4. **Waktu Pelatihan**:
   - Model BFS membutuhkan waktu pelatihan yang lebih lama (120 detik)
     dibandingkan dengan DFS (110 detik), menunjukkan trade-off antara performa
     dan efisiensi waktu.

### Kesimpulan Akhir

Dari analisis di atas, dapat disimpulkan bahwa model **BFS dengan oversampling**
memberikan performa terbaik dalam hal akurasi dan F1-score untuk kelas
**Non-Predator**. Namun, model **DFS dengan oversampling** menunjukkan kemampuan
yang lebih baik dalam menangkap jurnal predator, meskipun dengan trade-off pada
precision. Oleh karena itu, jika tujuan utama adalah mendeteksi sebanyak mungkin
jurnal predator, model DFS dengan oversampling dapat dipertimbangkan.

### Next Step (8_3_final_evaluation)

Langkah selanjutnya adalah melakukan **evaluasi akhir** untuk menentukan model
terbaik berdasarkan hasil perbandingan ini dan melakukan analisis lebih lanjut
untuk meningkatkan performa model.

## 8_3_final_evaluation

Pada tahap ini, kami akan melakukan **evaluasi akhir** untuk menentukan model
terbaik berdasarkan hasil perbandingan antara model yang dilatih dengan data
yang telah di-oversampling dan model yang dilatih dengan data tanpa
oversampling. Evaluasi ini bertujuan untuk memberikan rekomendasi mengenai model
yang paling efektif dalam mengidentifikasi jurnal sebagai **predator**.

### Metodologi Evaluasi

Evaluasi akhir dilakukan dengan mempertimbangkan metrik-metrik berikut:

- **Akurasi**: Persentase prediksi yang benar dari total prediksi.
- **Precision**: Proporsi prediksi positif yang benar dari total prediksi
  positif.
- **Recall**: Proporsi prediksi positif yang benar dari total aktual positif.
- **F1-score**: Rata-rata harmonis dari precision dan recall, memberikan
  gambaran yang lebih baik tentang keseimbangan antara keduanya.
- **Waktu Pelatihan**: Total waktu yang dibutuhkan untuk melatih model.

### Hasil Evaluasi

Berdasarkan hasil perbandingan sebelumnya, berikut adalah ringkasan metrik
evaluasi untuk model terbaik:

| Metrik                       | Model Klasifikasi BFS (Oversampling) | Model Klasifikasi DFS (Oversampling) | Model Klasifikasi BFS (Tanpa Oversampling) | Model Klasifikasi DFS (Tanpa Oversampling) |
| ---------------------------- | ------------------------------------ | ------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| **Akurasi**                  | 91.32%                               | 86.75%                               | 88.10%                                     | 88.16%                                     |
| **Precision (Non-Predator)** | 0.9741                               | 0.9808                               | 0.9774                                     | 0.9797                                     |
| **Recall (Non-Predator)**    | 0.9305                               | 0.8734                               | 0.8915                                     | 0.8899                                     |
| **F1-score (Non-Predator)**  | 0.9518                               | 0.9240                               | 0.9324                                     | 0.9326                                     |
| **Precision (Predator)**     | 0.4659                               | 0.3502                               | 0.3736                                     | 0.3781                                     |
| **Recall (Predator)**        | 0.7100                               | 0.7993                               | 0.7584                                     | 0.7844                                     |
| **F1-score (Predator)**      | 0.5626                               | 0.4870                               | 0.5006                                     | 0.5103                                     |
| **Waktu Pelatihan (detik)**  | 120                                  | 110                                  | 90                                         | 85                                         |

### Rekomendasi Model

1. **Model Klasifikasi BFS dengan Oversampling**:

   - Direkomendasikan untuk akurasi dan F1-score yang baik untuk kelas
     **Non-Predator**.

2. **Model Klasifikasi DFS dengan Oversampling**:
   - Direkomendasikan jika fokus utama adalah menangkap lebih banyak jurnal
     predator, meskipun dengan trade-off pada precision.

### Kesimpulan

Berdasarkan evaluasi akhir, model **BFS dengan oversampling** direkomendasikan
sebagai model terbaik untuk klasifikasi jurnal sebagai predator atau
non-predator. Meskipun model ini memiliki trade-off dalam hal precision untuk
kelas **Predator**, akurasi dan metrik evaluasi lainnya menunjukkan performa
yang lebih baik secara keseluruhan.
