# Predatory Journal Classifier

## Deskripsi

Proyek ini bertujuan untuk mengklasifikasikan situs web jurnal menjadi **jurnal
predator** atau **non-predator** menggunakan **Doc2Vec** dan **AutoML berbasis
Pohon DOM**. Dataset yang digunakan berasal dari
[Predatory Research Journals Data (Kaggle)](https://www.kaggle.com/datasets/web3fahim/predatory-research-journals-data)
dan [Directory of Open Access Journals (DOAJ)](https://doaj.org/csv).

## Requirement

- Python **3.8.10** (Direkomendasikan untuk menghindari masalah kompatibilitas)
- Virtual environment **(opsional, direkomendasikan)**

### Ignored Datasets

Terkait data yang di **ignored** pada `.gitignore` karena ukurannya yang besar,
silahkan download data tersebut di link berikut:
[s.itk.ac.id/pjc_datasets](https://s.itk.ac.id/pjc_datasets).

Setelah mendownload, pindahkan file tersebut ke dalam direktori sesuai dengan
struktur proyek.

#### 3_scraped_journal_data

Untuk data `3_scraped_journal_data.json` harap di masukkan ke dalam folder
`3_scraped_journal_data`.

#### 4_preprocess_scraped_data

Untuk data `4_dfs_preprocess_scraped_data.json` dan
`4_bfs_preprocess_scraped_data.json` harap di masukkan ke dalam folder
`4_preprocess_scraped_data`.

#### 5_split_data

Untuk data `5_bfs_train.json` dan `5_dfs_train.json` harap di masukkan ke dalam
folder `5_split_data`.

## Installation

1. **Clone repository ini:**

   ```bash
   git clone https://github.com/ersankarimi/predatory-journal-classifier
   cd predatory-journal-classifier
   ```

2. **Buat dan aktifkan virtual environment (opsional tapi direkomendasikan):**

   - **Windows:**

     ```bash
     python3.8 -m venv .venv
     .venv\Scripts\activate
     ```

   - **Mac/Linux:**

     ```bash
      python3.8 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependensi proyek:**

   ```bash
   pip install -r requirements.txt
   ```

## Progress

Untuk progress detail bisa dilihat di [progress.md](progress.md).

## How to Use

### 1. Persiapan Dataset

Sebelum menjalankan skrip, pastikan dataset sudah tersedia dalam direktori
`datasets/`:

- **Dataset DOAJ**: `datasets/journalcsv__doaj_20250105_1420_utf8.csv`
- **Dataset Predatory**: `datasets/predatory_Journals.csv`

### 2. Langkah-langkah Pemrosesan

#### **Step 1: Penggabungan Dataset**

Gabungkan dataset DOAJ dan dataset predatory ke dalam satu file:

```bash
python scripts/1_combine_journal_data.py
```

**Output:**

- `1_combined_journal_data/combined_journal_data.csv`
- `1_combined_journal_data/combined_journal_data.log`

#### **Step 2: Filtering Data**

Hapus data duplikat dan data tanpa tautan:

```bash
python scripts/2_filter_journal_data.py
```

**Output:**

- `2_filtered_journal_data/filtered_journal_data.csv`
- `2_filtered_journal_data/filtered_journal_data_removed.csv`
- `2_filtered_journal_data/filtered_journal_data.log`
- `2_filtered_journal_data/filtered_journal_duplicates.log`

#### **Step 3: Scraping Data**

Ambil konten dari halaman jurnal menggunakan scraping:

```bash
python scripts/3_scrape_journal_data.py
```

**Output:**

- `3_scraped_journal_data/3_scraped_journal_data.json`
- `3_scraped_journal_data/3_scraped_journal_data_failed.json`
- `3_scraped_journal_data/3_scraped_journal_data.log`

#### **Step 4: Pra-pemrosesan Data**

Konversi struktur HTML menjadi representasi tekstual berbentuk **DOM corpus**:

```bash
python scripts/4_preprocess_scraped_data.py
```

**Output:**

- `4_preprocess_scraped_data/4_bfs_preprocess_scraped_data.json`
- `4_preprocess_scraped_data/4_dfs_preprocess_scraped_data.json`
- `4_preprocess_scraped_data/4_preprocess_scraped_data.log`

#### **Step 5: Pembagian Data**

Pisahkan dataset menjadi **data latih** dan **data uji** dengan rasio **80:20**:

```bash
python scripts/5_split_data.py
```

**Output:**

- `5_split_data/5_bfs_train.json`
- `5_split_data/5_bfs_test.json`
- `5_split_data/5_dfs_train.json`
- `5_split_data/5_dfs_test.json`
- `5_split_data/5_split_data.log`
- `5_split_data/5_split_summary.json`

#### **Step 6: ...**

_Akan diupdate seiring progress proyek._

## Project Structure

```bash
.
├── .venv/                          # Virtual environment (jika digunakan)
├── progress.md                      # Catatan progres proyek
├── README.md                        # Dokumentasi proyek
├── requirements.txt                  # Dependensi proyek
├── runtime.txt                       # Versi Python yang digunakan
│
├── datasets/                         # Dataset mentah
│   ├── journalcsv__doaj_20250105_1420_utf8.csv
│   ├── predatory_Journals.csv
│
├── 1_combine_journal_data.py         # Skrip penggabungan dataset
├── 1_combined_journal_data/          # Hasil penggabungan dataset
│   ├── 1_combined_journal_data.csv
│   ├── 1_combined_journal_data.log
│
├── 2_filter_journal_data.py          # Skrip penyaringan dataset
├── 2_filtered_journal_data/          # Hasil penyaringan dataset
│   ├── 2_filtered_journal_data.csv
│   ├── 2_filtered_journal_data_removed.csv
│   ├── 2_filtered_journal_duplicates.log
│   ├── 2_filtered_journal_data.log
│   ├── sample.csv
│
├── 3_scrape_journal_data.py          # Skrip scraping data jurnal
├── 3_scraped_journal_data/           # Hasil scraping data jurnal
│   ├── 3_scraped_journal_data.json   # Ignored karena ukurannya besar (lebih dari 6GB)
│   ├── 3_scraped_journal_data_failed.json
│   ├── 3_scraped_journal_data.log
│   ├── sample/
│   │   ├── scraped_journal_data.json
│   │   ├── scraped_journal_data_failed.json
│   │   ├── scraped_journal_data.log
│
├── 4_preprocess_scraped_data.py      # Skrip preprocessing data jurnal
├── 4_preprocess_scraped_data/        # Hasil preprocessing data jurnal
│   ├── 4_bfs_preprocess_scraped_data.json
│   ├── 4_dfs_preprocess_scraped_data.json
│   ├── 4_preprocess_scraped_data.log
│
├── 5_split_data.py                   # Skrip pemisahan data jurnal
├── 5_split_data/                     # Hasil pemisahan data jurnal
│   ├── 5_bfs_train.json
│   ├── 5_bfs_test.json
│   ├── 5_dfs_train.json
│   ├── 5_dfs_test.json
│   ├── 5_split_data.log
│   ├── 5_split_summary.json
│
├── 6_vectorize_journal_data.py        # Skrip vektorisasi data jurnal
├── 6_1_lookup.py                     # Skrip pengecekan model Doc2Vec
├── 6_vectorized_journal_data/         # Hasil vektorisasi data jurnal
│   ├── 6_1_lookup.log
│   ├── 6_bfs_train_vectors.npy
│   ├── 6_bfs_test_vectors.npy
│   ├── 6_dfs_train_vectors.npy
│   ├── 6_dfs_test_vectors.npy
│   ├── 6_doc2vec_bfs_train.model
│   ├── 6_doc2vec_dfs_train.model
│   ├── 6_execution_time.json
│   ├── 6_vectorization.log
│
├── 7_oversampling.py                  # Skrip oversampling untuk data pelatihan
├── 7_oversampling/                    # Hasil oversampling
│   ├── 7_bfs_train_vectors_oversampled.npy
│   ├── 7_bfs_train_labels_oversampled.npy
│   ├── 7_dfs_train_vectors_oversampled.npy
│   ├── 7_dfs_train_labels_oversampled.npy
│   ├── 7_oversampling.log
│
├── ...                                 # Step selanjutnya yang akan diperbarui seiring progress proyek
```
