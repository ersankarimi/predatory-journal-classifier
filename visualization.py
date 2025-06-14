import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data dari classification reports
data = {
    "Metode": ["BFS"] * 3 + ["DFS"] * 8,
    "Waktu": [10, 105, 120, 10, 15, 30, 45, 60, 90, 105, 120],
    "Akurasi": [
        0.8409,
        0.8459,
        0.8257,
        0.8436,
        0.8360,
        0.8266,
        0.8485,
        0.8383,
        0.8582,
        0.8579,
        0.8067,
    ],
    "Precision_Predator": [
        0.2932,
        0.3141,
        0.2879,
        0.3021,
        0.2926,
        0.2787,
        0.3133,
        0.3033,
        0.3302,
        0.3323,
        0.2639,
    ],
    "Recall_Predator": [
        0.7249,
        0.8104,
        0.8253,
        0.7546,
        0.7658,
        0.7584,
        0.7770,
        0.8141,
        0.7807,
        0.7993,
        0.8141,
    ],
    "F1_Predator": [
        0.4176,
        0.4528,
        0.4269,
        0.4315,
        0.4234,
        0.4076,
        0.4466,
        0.4420,
        0.4641,
        0.4694,
        0.3985,
    ],
}

df = pd.DataFrame(data)

# Konfigurasi Seaborn
sns.set(style="whitegrid")
colors = sns.color_palette("husl", 2)

# Daftar metrik yang akan diplot
metrics = ["Akurasi", "Precision_Predator", "Recall_Predator", "F1_Predator"]

# Membuat Subplot
fig, axes = plt.subplots(
    len(metrics), 1, figsize=(10, 6 * len(metrics)), sharex=True
)

# Looping untuk membuat plot untuk setiap metrik
for i, metric in enumerate(metrics):
    # Plot BFS
    sns.lineplot(
        ax=axes[i],
        data=df[df["Metode"] == "BFS"],
        x="Waktu",
        y=metric,
        label="BFS",
        marker="o",
        color=colors[0],
    )

    # Plot DFS
    sns.lineplot(
        ax=axes[i],
        data=df[df["Metode"] == "DFS"],
        x="Waktu",
        y=metric,
        label="DFS",
        marker="o",
        color=colors[1],
    )

    axes[i].set_title(f"{metric} vs. Waktu", fontsize=14)
    axes[i].set_ylabel(metric, fontsize=12)
    axes[i].tick_params(axis="x", rotation=45)
    axes[i].legend()


# Menambahkan judul keseluruhan
fig.suptitle(
    "Perbandingan Performa BFS vs DFS (No Oversampling)", fontsize=16, y=0.92
)

# Menampilkan Plot
plt.tight_layout(rect=[0, 0, 1, 0.90])
plt.show()

# Menyimpan Plot
fig.savefig("perbandingan_bfs_dfs_no_oversampling_lengkap.png", dpi=300)
