import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data hasil metrik (update)
data = {
    'Waktu': [10, 15, 30, 45, 60, 75, 90, 105, 120],
    'BFS_Accuracy': [0.9168, 0.9196, 0.9020, 0.8837, 0.8816, 0.9106, 0.9143, 0.8816, 0.8862],
    'BFS_F1_MacroAvg': [0.7804, 0.7812, 0.7639, 0.7401, 0.7377, 0.7711, 0.7779, 0.7377, 0.7436],
    'DFS_Accuracy': [0.8902, 0.9202, 0.8902, 0.9134, 0.9045, 0.9252, 0.9255, 0.9088, 0.9171],
    'DFS_F1_MacroAvg': [0.7229, 0.7829, 0.7229, 0.7711, 0.7645, 0.7848, 0.7853, 0.7663, 0.7809]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Mengatur style seaborn
sns.set(style="whitegrid")

# Membuat subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 12))
fig.suptitle('Perbandingan Akurasi dan F1-Score Macro Avg antara BFS dan DFS terhadap Waktu', fontsize=16)

# Daftar metrik yang akan diplot
metrics = ['Accuracy', 'F1_MacroAvg']

# Loop untuk membuat plot untuk setiap metrik
for i, metric in enumerate(metrics):
    ax = axes[i]
    ax.plot(df['Waktu'], df[f'BFS_{metric}'], marker='o', label='BFS')
    ax.plot(df['Waktu'], df[f'DFS_{metric}'], marker='o', label='DFS')
    ax.set_xlabel('Waktu (Menit)')
    ax.set_ylabel(metric)
    ax.set_title(f'Perbandingan {metric}')
    ax.set_xticks(df['Waktu'])
    ax.legend()
    ax.grid(True)

# Menyesuaikan tata letak dan simpan sebagai gambar
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('perbandingan_akurasi_f1.png')
plt.show()
