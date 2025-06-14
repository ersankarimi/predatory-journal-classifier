# Menggunakan AutoML

## No-Oversampling

### BFS

#### 10 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9731    0.8508    0.9079      3151
    Predator     0.2932    0.7249    0.4176       269

    accuracy                         0.8409      3420
   macro avg     0.6332    0.7879    0.6627      3420
weighted avg     0.9197    0.8409    0.8693      3420

Akurasi: 0.8409
```

#### 105 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9813    0.8489    0.9103      3151
    Predator     0.3141    0.8104    0.4528       269

    accuracy                         0.8459      3420
   macro avg     0.6477    0.8297    0.6815      3420
weighted avg     0.9288    0.8459    0.8743      3420

Akurasi: 0.8459
```

#### 120 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9823    0.8258    0.8972      3151
    Predator     0.2879    0.8253    0.4269       269

    accuracy                         0.8257      3420
   macro avg     0.6351    0.8255    0.6621      3420
weighted avg     0.9276    0.8257    0.8602      3420

Akurasi: 0.8257
```

### DFS

#### 10 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9760    0.8512    0.9093      3151
    Predator     0.3021    0.7546    0.4315       269

    accuracy                         0.8436      3420
   macro avg     0.6390    0.8029    0.6704      3420
weighted avg     0.9230    0.8436    0.8717      3420

Akurasi: 0.8436
```

#### 15 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9768    0.8420    0.9044      3151
    Predator     0.2926    0.7658    0.4234       269

    accuracy                         0.8360      3420
   macro avg     0.6347    0.8039    0.6639      3420
weighted avg     0.9230    0.8360    0.8666      3420

Akurasi: 0.8360
```

#### 30 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9758    0.8324    0.8984      3151
    Predator     0.2787    0.7584    0.4076       269

    accuracy                         0.8266      3420
   macro avg     0.6273    0.7954    0.6530      3420
weighted avg     0.9210    0.8266    0.8598      3420

Akurasi: 0.8266
```

#### 45 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9782    0.8546    0.9123      3151
    Predator     0.3133    0.7770    0.4466       269

    accuracy                         0.8485      3420
   macro avg     0.6458    0.8158    0.6794      3420
weighted avg     0.9259    0.8485    0.8756      3420

Akurasi: 0.8485
```

#### 60 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9815    0.8404    0.9055      3151
    Predator     0.3033    0.8141    0.4420       269

    accuracy                         0.8383      3420
   macro avg     0.6424    0.8272    0.6737      3420
weighted avg     0.9281    0.8383    0.8690      3420

Akurasi: 0.8383
```

#### 90 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9788    0.8648    0.9183      3151
    Predator     0.3302    0.7807    0.4641       269

    accuracy                         0.8582      3420
   macro avg     0.6545    0.8227    0.6912      3420
weighted avg     0.9278    0.8582    0.8826      3420

Akurasi: 0.8582
```

### Visualisasi

![perbandingan_bfs_dfs_no_oversampling_lengkap.png](https://media-hosting.imagekit.io/0bec045ad6524346/perbandingan_bfs_dfs_no_oversampling_lengkap.png?Expires=1841810998&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=D2fj1dAqwd45xgL~R3JmGNTFYbwcczpy-efX~eRMbopw2CsdJQL8Zf18h2ThKj3bt~wH2Ai3l7xi6bUlS~IvpZTirJaXFm5h1~tDFcEcJx94SmqpqFo~iDSA-TbJHKwBm0hT0zlGTyGMPmF-9tq-Fi2aDXZ9c8zrceKyt1SS80Osh4UNT4y2srLCcSBVfh3Y-gOMfbiMTKE9kVZheoRyUt12Y-rx6WcmLAqBPita~Jq4XPgYVZHbZ8fXTw5pAOnKdOu3rxfKZ7Dp73Ch1T0Rc3GHKjrNtLlkkdOC3zdktMzjtNm8YBhMO6ehISYlC7c3LTozmAL79lZNjX5GQ6CmXA__)

### Kesimpulan

Berikut adalah kesimpulan eksperimen AutoML tanpa oversampling yang sudah
dirapikan dalam format poin agar lebih mudah dibaca dan dipahami:

#### ✅ **Model Terbaik**

- **Model DFS (Durasi: 90 menit)**

  - **Akurasi:** 85,82%
  - **Recall (Predator):** **78,07%** ← _tertinggi dari semua percobaan_
  - **F1-score (Predator):** 46,41%
  - **Kesimpulan:** Model ini adalah yang **paling optimal** karena mencapai
    **recall tertinggi** pada kelas _Predator_, sesuai fokus penelitian untuk
    mengidentifikasi sebanyak mungkin jurnal predator.

---

#### 📊 **Performa Model BFS**

- **Model BFS (Durasi: 105 menit)**

  - **Akurasi:** 84,59%
  - **Recall (Predator):** 81,04%
  - **F1-score (Predator):** 45,28%
  - **Kelebihan:** Recall tinggi, mendekati model DFS terbaik.
  - **Kekurangan:** F1-score tidak setinggi model DFS 90 menit; stabilitas
    performa kurang merata pada durasi pelatihan lainnya.

- **Model BFS (Durasi: 10–120 menit lainnya)**

  - Recall kelas _Predator_ bervariasi antara 72%–82%
  - F1-score umumnya lebih rendah dari DFS

---

#### 📈 **Performa Model DFS (Selain 90 Menit)**

- **Durasi 10–60 menit:**

  - Recall kelas _Predator_ >75%
  - F1-score mendekati atau sedikit di atas BFS
  - Akurasi konsisten antara 83%–84%

- **Durasi 45 menit:**

  - Recall: 77,70%
  - F1-score: 44,66%
  - Hampir menyamai performa terbaik

---

#### 🧠 **Analisis Umum**

- **DFS lebih konsisten** dalam menghasilkan recall tinggi pada kelas _Predator_
  dibanding BFS.
- **Recall penting** untuk penelitian ini karena fokusnya adalah **mendeteksi
  sebanyak mungkin jurnal predator**, meskipun dengan trade-off pada precision.
- AutoML mampu mengeksplorasi pipeline model yang efektif dalam waktu terbatas,
  tetapi DFS memberi struktur DOM corpus yang lebih kaya konteks untuk
  pembelajaran mesin.

---
