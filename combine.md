# Menggunakan AutoML

## Oversampling

### BFS

#### 10 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9738    0.9188    0.9455      3151
    Predator     0.4273    0.7100    0.5335       269

    accuracy                         0.9023      3420
   macro avg     0.7005    0.8144    0.7395      3420
weighted avg     0.9308    0.9023    0.9131      3420

Akurasi: 0.9023
```

#### 15 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9754    0.9188    0.9462      3151
    Predator     0.4336    0.7286    0.5437       269

    accuracy                         0.9038      3420
   macro avg     0.7045    0.8237    0.7450      3420
weighted avg     0.9328    0.9038    0.9146      3420

Akurasi: 0.9038
```

#### 30 menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9753    0.9162    0.9449      3151
    Predator     0.4261    0.7286    0.5377       269

    accuracy                         0.9015      3420
   macro avg     0.7007    0.8224    0.7413      3420
weighted avg     0.9321    0.9015    0.9128      3420

Akurasi: 0.9015
```

#### 45 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9733    0.9264    0.9493      3151
    Predator     0.4489    0.7026    0.5478       269

    accuracy                         0.9088      3420
   macro avg     0.7111    0.8145    0.7485      3420
weighted avg     0.9321    0.9088    0.9177      3420

Akurasi: 0.9088
```

#### 60 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9774    0.9181    0.9468      3151
    Predator     0.4391    0.7509    0.5542       269

    accuracy                         0.9050      3420
   macro avg     0.7082    0.8345    0.7505      3420
weighted avg     0.9350    0.9050    0.9159      3420

Akurasi: 0.9050
```

#### 90 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9708    0.9280    0.9489      3151
    Predator     0.4436    0.6729    0.5347       269

    accuracy                         0.9079      3420
   macro avg     0.7072    0.8004    0.7418      3420
weighted avg     0.9293    0.9079    0.9163      3420

Akurasi: 0.9079
```

#### 105 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9697    0.9349    0.9520      3151
    Predator     0.4634    0.6580    0.5438       269

    accuracy                         0.9132      3420
   macro avg     0.7165    0.7965    0.7479      3420
weighted avg     0.9299    0.9132    0.9199      3420

Akurasi: 0.9132
```

#### 120 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9698    0.9372    0.9532      3151
    Predator     0.4720    0.6580    0.5497       269

    accuracy                         0.9152      3420
   macro avg     0.7209    0.7976    0.7514      3420
weighted avg     0.9306    0.9152    0.9215      3420

Akurasi: 0.9152
```

### DFS

#### 10 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9831    0.9019    0.9407      3151
    Predator     0.4159    0.8178    0.5514       269

    accuracy                         0.8953      3420
   macro avg     0.6995    0.8599    0.7461      3420
weighted avg     0.9384    0.8953    0.9101      3420

Akurasi: 0.8953
```

#### 15 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9814    0.8873    0.9320      3151
    Predator     0.3783    0.8030    0.5143       269

    accuracy                         0.8807      3420
   macro avg     0.6798    0.8452    0.7231      3420
weighted avg     0.9340    0.8807    0.8991      3420

Akurasi: 0.8807
```

#### 30 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9803    0.9010    0.9390      3151
    Predator     0.4046    0.7881    0.5347       269

    accuracy                         0.8921      3420
   macro avg     0.6924    0.8445    0.7368      3420
weighted avg     0.9350    0.8921    0.9072      3420

Akurasi: 0.8921
```

#### 45 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9775    0.9105    0.9428      3151
    Predator     0.4186    0.7546    0.5385       269

    accuracy                         0.8982      3420
   macro avg     0.6980    0.8326    0.7406      3420
weighted avg     0.9335    0.8982    0.9110      3420

Akurasi: 0.8982
```

#### 60 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9812    0.8930    0.9350      3151
    Predator     0.3895    0.7993    0.5238       269

    accuracy                         0.8857      3420
   macro avg     0.6853    0.8462    0.7294      3420
weighted avg     0.9346    0.8857    0.9027      3420

Akurasi: 0.8857
```

#### 75 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9754    0.9070    0.9400      3151
    Predator     0.4020    0.7323    0.5191       269

    accuracy                         0.8933      3420
   macro avg     0.6887    0.8197    0.7295      3420
weighted avg     0.9303    0.8933    0.9069      3420

Akurasi: 0.8933
```

#### 90 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9843    0.8556    0.9154      3151
    Predator     0.3319    0.8401    0.4758       269

    accuracy                         0.8544      3420
   macro avg     0.6581    0.8479    0.6956      3420
weighted avg     0.9330    0.8544    0.8809      3420

Akurasi: 0.8544
```

#### 105 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9692    0.9375    0.9531      3151
    Predator     0.4704    0.6506    0.5460       269

    accuracy                         0.9149      3420
   macro avg     0.7198    0.7940    0.7495      3420
weighted avg     0.9299    0.9149    0.9210      3420

Akurasi: 0.9149
```

#### 120 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9809    0.8975    0.9374      3151
    Predator     0.3985    0.7955    0.5310       269

    accuracy                         0.8895      3420
   macro avg     0.6897    0.8465    0.7342      3420
weighted avg     0.9351    0.8895    0.9054      3420

Akurasi: 0.8895
```

---

### Oversampling Visualization

![perbandingan_bfs_dfs_oversampling.png](https://media-hosting.imagekit.io/84e32f1c9efb4845/perbandingan_bfs_dfs_oversampling.png?Expires=1841810296&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=YJmDQwNfAMv5rnOtPwejqLuImf5N0Q6ZtspYYsqG0YzcYC2dHUFXzMqS-nPWHFwcnaOqbZ80pnzeH0-7PgrUQayoRKJkhdB4iNaKZyr-iujotTpCS1kV1Y5FfaNfKfurSt6Tok98BNWb~DrnV1pqTEmrSyUbdqgZEx31vt47B9UE-KjiA9cgQO8-OsT63zSYKMlfkkV04Og7mi1E33sFDl7j5OdIhjX~kxtfFDifRZpIrKfy7kWJrP0JkdjTNSWJV28p5lps9WmhsGLsAWxJ-ByzepEqE-iY9I~2kaq6PPErrie1oSqIqGb-0njETfIW0krAbLv2DZQFQ9FA7frRRg__)

### Kesimpulan

Berdasarkan hasil eksperimen klasifikasi web jurnal predator menggunakan AutoML
dengan metode oversampling SMOTEENN dan variasi traversal DOM (BFS dan DFS),
dapat disimpulkan beberapa hal sebagai berikut:

1. **Performa Model secara Umum** Baik metode BFS maupun DFS menunjukkan akurasi
   model yang cukup tinggi secara keseluruhan (> 0.88). Namun, akurasi bukan
   satu-satunya acuan karena kelas _Predator_ merupakan fokus utama dalam
   penelitian ini. Oleh karena itu, metrik _recall_ pada kelas _Predator_
   menjadi perhatian utama.

2. **Perbandingan BFS dan DFS**

   - Traversal **BFS** cenderung menghasilkan nilai _recall_ kelas _Predator_
     yang stabil dan cukup tinggi, terutama pada durasi pelatihan 60–120 menit,
     dengan nilai _recall_ mencapai 0.7509 (60 menit) dan 0.6580 (120 menit).
   - Traversal **DFS** pada beberapa durasi (misalnya 10 dan 30 menit) mampu
     mencapai nilai _recall_ tinggi seperti 0.8178 dan 0.7881. Namun, kestabilan
     performanya kurang konsisten dibandingkan BFS. DFS juga menunjukkan
     penurunan performa pada beberapa durasi lebih lama (misalnya 90 menit).

3. **Durasi Optimal** Durasi pelatihan memengaruhi performa, namun peningkatan
   waktu tidak selalu menghasilkan performa yang lebih baik. Durasi **105–120
   menit** untuk kedua traversal menunjukkan performa paling seimbang antara
   _recall_, _f1-score_, dan akurasi. Pada titik ini, BFS mencatat akurasi
   0.9152 dan DFS 0.9149, dengan _recall_ pada kelas _Predator_ masing-masing
   sebesar 0.6580 dan 0.6506.

4. **Rekomendasi** Untuk prioritas utama adalah **mendeteksi sebanyak mungkin
   jurnal predator** (yaitu _recall_ tinggi), maka **BFS dengan durasi pelatihan
   60 hingga 120 menit** menjadi pilihan yang paling disarankan karena
   memberikan performa stabil, recall tinggi, dan akurasi di atas 90%. Sementara
   itu, DFS tetap merupakan alternatif yang kuat, terutama jika mempertimbangkan
   eksplorasi struktur DOM yang lebih dalam.

---

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

#### 105 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9805    0.8629    0.9180      3151
    Predator     0.3323    0.7993    0.4694       269

    accuracy                         0.8579      3420
   macro avg     0.6564    0.8311    0.6937      3420
weighted avg     0.9295    0.8579    0.8827      3420

Akurasi: 0.8579
```

#### 120 Menit

```bash
              precision    recall  f1-score   support

Non-Predator     0.9807    0.8061    0.8849      3151
    Predator     0.2639    0.8141    0.3985       269

    accuracy                         0.8067      3420
   macro avg     0.6223    0.8101    0.6417      3420
weighted avg     0.9243    0.8067    0.8466      3420

Akurasi: 0.8067
```

### Visualisasi

![perbandingan_bfs_dfs_no_oversampling_lengkap.png](https://ik.imagekit.io/ef7zqewbd/perbandingan_bfs_dfs_no_oversampling_lengkap.png?updatedAt=1747288044706)

### Kesimpulan

Berikut adalah kesimpulan eksperimen AutoML **tanpa oversampling**:

#### Model Terbaik

- **DFS (105 menit):** Akurasi 85.79%, Recall (Predator) 79.93%, F1-score
  (Predator) 46.94%. Model ini menawarkan keseimbangan yang baik antara akurasi
  dan recall untuk kelas Predator.

#### Performa Model Lainnya

- **DFS (120 menit):** Memiliki Recall (Predator) tertinggi (81.41%), namun
  dengan presisi yang rendah (26.39%) sehingga menghasilkan F1-score yang juga
  rendah (39.85%). Ini menunjukkan trade-off antara kemampuan mendeteksi
  Predator dengan risiko kesalahan klasifikasi yang lebih tinggi.
- **DFS (Durasi 10–90 menit):** Recall untuk kelas Predator bervariasi antara
  75.46% dan 78.07%. Model-model ini memiliki F1-score yang lebih rendah
  dibandingkan dengan model DFS 105 menit.

- **BFS (10 menit):** Akurasi 84.09%, Recall (Predator) 72.49%, F1-score
  (Predator) 41.76%
- **BFS (105 menit):** Akurasi 84.59%, Recall (Predator) 81.04%, F1-score
  (Predator) 45.28%
- **BFS (120 menit):** Akurasi 82.57%, Recall (Predator) 82.53%, F1-score
  (Predator) 42.69%

#### Analisis Umum

- Secara umum, model dengan algoritma DFS cenderung menunjukkan _recall_ yang
  lebih tinggi untuk kelas _Predator_, namun seringkali dengan mengorbankan
  _presisi_.
- Model **DFS (105 menit)** memberikan keseimbangan yang cukup baik antara
  _recall_ dan _presisi_, sehingga menjadi pilihan yang layak sebagai model
  terbaik dalam eksperimen ini.
- Algoritma DFS mungkin lebih efektif dalam mengeksplorasi fitur-fitur yang
  relevan untuk mengidentifikasi jurnal predator dalam dataset ini.
- Fokus pada metrik _recall_ terpenuhi, terutama dengan model DFS berdurasi 105
  menit dan 120 menit, meskipun model 120 menit memiliki _presisi_ yang rendah.

# Menggunakan NCM dan Hierarchical Clustering

## Oversampling

### BFS

#### n_clusters=2, linkage='ward' (60.78 detik)

```bash
              precision    recall  f1-score   support

Non-Predator     0.0000    0.0000    0.0000      3151
    Predator     0.0787    1.0000    0.1458       269

    accuracy                         0.0787      3420
   macro avg     0.0393    0.5000    0.0729      3420
weighted avg     0.0062    0.0787    0.0115      3420

Akurasi: 0.0787
```

#### n_clusters=2, linkage='complete' (65.08 detik)

```bash
              precision    recall  f1-score   support

Non-Predator     0.0000    0.0000    0.0000      3151
    Predator     0.0787    1.0000    0.1458       269

    accuracy                         0.0787      3420
   macro avg     0.0393    0.5000    0.0729      3420
weighted avg     0.0062    0.0787    0.0115      3420

Akurasi: 0.0787
```

#### n_clusters=2, linkage='average' (61.30 detik)

```bash
              precision    recall  f1-score   support

Non-Predator     0.0000    0.0000    0.0000      3151
    Predator     0.0787    1.0000    0.1458       269

    accuracy                         0.0787      3420
   macro avg     0.0393    0.5000    0.0729      3420
weighted avg     0.0062    0.0787    0.0115      3420

Akurasi: 0.0787
```

#### n_clusters=3, linkage='ward' (57.06 detik)

```bash
              precision    recall  f1-score   support

Non-Predator     1.0000    1.0000    1.0000      3151
    Predator     0.0000    0.0000    0.0000       269

    accuracy                         1.0000      3420
   macro avg     0.5000    0.5000    0.5000      3420
weighted avg     1.0000    1.0000    1.0000      3420

Akurasi: 1.0000
```

#### n_clusters=3, linkage='complete' (58.90 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=3, linkage='average' (59.49 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=4, linkage='ward' (57.67 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.9961    0.0812    0.1502      3151
    Predator     0.0847    0.9963    0.1562       269

    accuracy                         0.1532      3420
   macro avg     0.5404    0.5388    0.1532      3420
weighted avg     0.9244    0.1532    0.1507      3420

Akurasi: 0.1532
```

#### n_clusters=4, linkage='complete' (58.21 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=4, linkage='average' (59.93 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=5, linkage='ward' (56.97 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.9785    0.1882    0.3157      3151
    Predator     0.0910    0.9517    0.1661       269

    accuracy                         0.2482      3420
   macro avg     0.5348    0.5699    0.2409      3420
weighted avg     0.9087    0.2482    0.3039      3420

Akurasi: 0.2482
```

#### n_clusters=5, linkage='complete' (58.82 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=5, linkage='average' (59.64 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0006    0.0013      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0792      3420
   macro avg     0.5394    0.5003    0.0736      3420
weighted avg     0.9275    0.0792    0.0126      3420

Akurasi: 0.0792
```

#### Hasil Terbaik

```bash
              precision    recall  f1-score   support
Non-Predator     0.9378    0.7753    0.8489      3151
    Predator     0.1313    0.3978    0.1974       269

    accuracy                         0.7456      3420
   macro avg     0.5346    0.5865    0.5231      3420
weighted avg     0.8744    0.7456    0.7976      3420

Akurasi: 0.7456
```

---

### DFS

#### n_clusters=2, linkage=ward (57.63 detik)

```bash
              precision    recall  f1-score   support

Non-Predator     0.0000    0.0000    0.0000      3151
    Predator     0.0787    1.0000    0.1458       269

    accuracy                         0.0787      3420
   macro avg     0.0393    0.5000    0.0729      3420
weighted avg     0.0062    0.0787    0.0115      3420

Akurasi: 0.0787
```

#### n_clusters=2, linkage=complete (58.75 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.0000    0.0000    0.0000      3151
    Predator     0.0787    1.0000    0.1458       269

    accuracy                         0.0787      3420
   macro avg     0.0393    0.5000    0.0729      3420
weighted avg     0.0062    0.0787    0.0115      3420

Akurasi: 0.0787
```

#### n_clusters=2, linkage=average (59.88 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=3, linkage=ward (57.42 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.9586    0.5217    0.6757      3151
    Predator     0.1161    0.7361    0.2006       269

    accuracy                         0.5386      3420
   macro avg     0.5374    0.6289    0.4382      3420
weighted avg     0.8923    0.5386    0.6383      3420

Akurasi: 0.5386
```

#### n_clusters=3, linkage=complete (59.31 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=3, linkage=average (60.50 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=4, linkage=ward (58.34 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.9886    0.3564    0.5239      3151
    Predator     0.1121    0.9517    0.2005       269

    accuracy                         0.4032      3420
   macro avg     0.5503    0.6540    0.3622      3420
weighted avg     0.9196    0.4032    0.4985      3420

Akurasi: 0.4032
```

#### n_clusters=4, linkage=complete (59.13 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=4, linkage=average (60.72 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### n_clusters=5, linkage=ward (61.46 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     0.9897    0.3351    0.5007      3151
    Predator     0.1096    0.9591    0.1968       269

    accuracy                         0.3842      3420
   macro avg     0.5497    0.6471    0.3488      3420
weighted avg     0.9205    0.3842    0.4768      3420
```

#### n_clusters=5, linkage=complete (65.27 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0019    0.0038      3151
    Predator     0.0788    1.0000    0.1461       269

    accuracy                         0.0804      3420
   macro avg     0.5394    0.5010    0.0749      3420
weighted avg     0.9275    0.0804    0.0150      3420

Akurasi: 0.0804
```

#### n_clusters=5, linkage=average (65.43 detik)

```bash
              precision    recall  f1-score   support
Non-Predator     1.0000    0.0003    0.0006      3151
    Predator     0.0787    1.0000    0.1459       269

    accuracy                         0.0789      3420
   macro avg     0.5393    0.5002    0.0733      3420
weighted avg     0.9275    0.0789    0.0121      3420

Akurasi: 0.0789
```

#### Hasil Terbaik

```bash
              precision    recall  f1-score   support
Non-Predator     0.9586    0.5217    0.6757      3151
    Predator     0.1161    0.7361    0.2006       269

    accuracy                         0.5386      3420
   macro avg     0.5374    0.6289    0.4382      3420
weighted avg     0.8923    0.5386    0.6383      3420

Akurasi: 0.5386
```

---
