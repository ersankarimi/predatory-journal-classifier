import matplotlib.pyplot as plt
import numpy as np

# Data dari hasil metrik terbaru
data = {
    'Metrics': ['Accuracy', 'F1_MacroAvg'],
    'AutoML_DFS_90': [0.9255, 0.7853],
    'HC_NCM': [0.8859, 0.7343]
}

# Mengatur posisi bar
pos = np.arange(len(data['Metrics']))
bar_width = 0.35

# Membuat plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.bar(pos - bar_width / 2, data['AutoML_DFS_90'], bar_width, label='AutoML DFS 90 Menit')
plt.bar(pos + bar_width / 2, data['HC_NCM'], bar_width, label='HC + NCM')

# Menambahkan label dan judul
plt.xlabel('Metrik')
plt.ylabel('Skor')
plt.title('Perbandingan Akurasi dan F1-Score Macro Avg')
plt.xticks(pos, data['Metrics'])
plt.legend()

# Menambahkan grid
plt.grid(axis='y', alpha=0.7)

# Menambahkan anotasi nilai di atas bar
for i in pos:
    plt.text(i - bar_width / 2, data['AutoML_DFS_90'][i] + 0.01, str(round(data['AutoML_DFS_90'][i], 4)),
             ha='center', va='bottom')
    plt.text(i + bar_width / 2, data['HC_NCM'][i] + 0.01, str(round(data['HC_NCM'][i], 4)),
             ha='center', va='bottom')

# Menyimpan plot sebagai gambar
plt.tight_layout()
plt.savefig('perbandingan_akurasi_f1_macro_hcncm.png')

# Menampilkan plot
plt.show()
