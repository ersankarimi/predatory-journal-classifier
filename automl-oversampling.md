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

## Oversampling Visualization

![perbandingan_bfs_dfs_oversampling.png](https://media-hosting.imagekit.io/84e32f1c9efb4845/perbandingan_bfs_dfs_oversampling.png?Expires=1841810296&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=YJmDQwNfAMv5rnOtPwejqLuImf5N0Q6ZtspYYsqG0YzcYC2dHUFXzMqS-nPWHFwcnaOqbZ80pnzeH0-7PgrUQayoRKJkhdB4iNaKZyr-iujotTpCS1kV1Y5FfaNfKfurSt6Tok98BNWb~DrnV1pqTEmrSyUbdqgZEx31vt47B9UE-KjiA9cgQO8-OsT63zSYKMlfkkV04Og7mi1E33sFDl7j5OdIhjX~kxtfFDifRZpIrKfy7kWJrP0JkdjTNSWJV28p5lps9WmhsGLsAWxJ-ByzepEqE-iY9I~2kaq6PPErrie1oSqIqGb-0njETfIW0krAbLv2DZQFQ9FA7frRRg__)

## Kesimpulan

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

4. **Rekomendasi** Jika prioritas utama adalah **mendeteksi sebanyak mungkin
   jurnal predator** (yaitu _recall_ tinggi), maka **BFS dengan durasi pelatihan
   60 hingga 120 menit** menjadi pilihan yang paling disarankan karena
   memberikan performa stabil, recall tinggi, dan akurasi di atas 90%. Sementara
   itu, DFS tetap merupakan alternatif yang kuat, terutama jika mempertimbangkan
   eksplorasi struktur DOM yang lebih dalam.

---
