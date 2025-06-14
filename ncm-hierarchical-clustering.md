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

\

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
