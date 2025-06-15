import os
import json
import logging
import ijson

OUTPUT_DIR = "4_preprocess_scraped_data_sample"
os.makedirs(OUTPUT_DIR, exist_ok=True)

JSON_DFS = os.path.join(OUTPUT_DIR, "4_dfs_preprocess_scraped_data.json")
JSON_BFS = os.path.join(OUTPUT_DIR, "4_bfs_preprocess_scraped_data.json")
LOG_FILE = os.path.join(OUTPUT_DIR, "4_preprocess_scraped_data.log")

SCRAPED_FILE = "3_scraped_journal_data/3_scraped_journal_data.json"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
    ],
)

logger = logging.getLogger("preprocess")


def extract_tags_dfs(dom_structure):
    """Menelusuri DOM Tree dengan DFS untuk ekstraksi tag."""
    tags = []

    def dfs(node):
        if isinstance(node, list):
            for item in node:
                if item.get("tag"):
                    tags.append(item["tag"])
                if item.get("children"):
                    dfs(item["children"])

    dfs(dom_structure)
    return tags


def extract_tags_bfs(dom_structure):
    """Menelusuri DOM Tree dengan BFS untuk ekstraksi tag."""
    tags = []
    queue = [dom_structure]

    while queue:
        node = queue.pop(0)
        if isinstance(node, dict):
            if node.get("tag"):
                tags.append(node["tag"])
            if node.get("children"):
                queue.extend(node["children"])
        elif isinstance(node, list):
            queue.extend(node)

    return tags


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    logger.info("=" * 80)
    logger.info("🚀 Memulai proses ekstraksi DOM corpus...")

    # Load data hasil scraping menggunakan streaming JSON
    all_tags_dfs = []
    all_tags_bfs = []
    total_journals = 0
    total_predatory = 0
    total_non_predatory = 0

    try:
        with open(SCRAPED_FILE, "r", encoding="utf-8") as f:
            journals = ijson.items(f, "item")
            for idx, journal in enumerate(journals, start=1):
                total_journals += 1
                journal_title = journal.get("journal_title", "Unknown")
                journal_url = journal.get("journal_url", "Unknown")
                dom_structure = journal.get("dom_structure", {})
                is_predatory = journal.get("is_predatory", False)

                if is_predatory:
                    total_predatory += 1
                else:
                    total_non_predatory += 1

                logger.info(f"[{idx}] Memproses: {journal_title} | {journal_url}")

                tags_dfs = extract_tags_dfs(dom_structure)
                all_tags_dfs.append(
                    {
                        "journal_title": journal_title,
                        "journal_url": journal_url,
                        "is_predatory": is_predatory,
                        "dom_corpus": tags_dfs,
                    }
                )

                tags_bfs = extract_tags_bfs(dom_structure)
                all_tags_bfs.append(
                    {
                        "journal_title": journal_title,
                        "journal_url": journal_url,
                        "is_predatory": is_predatory,
                        "dom_corpus": tags_bfs,
                    }
                )

                # Log progress setiap 100 jurnal
                if idx % 100 == 0:
                    logger.info(f"📌 Progress: {idx} jurnal telah diproses...")

    except Exception as e:
        logger.error(f"❌ Error saat membaca JSON: {e}")
        exit(1)

    logger.info("=" * 80)
    logger.info(f"📊 Total jurnal yang diproses: {total_journals}")
    logger.info(f"   - Jurnal predator: {total_predatory}")
    logger.info(f"   - Jurnal non-predator: {total_non_predatory}")
    logger.info("=" * 80)

    # Simpan hasil ekstraksi ke JSON
    if all_tags_dfs:
        with open(JSON_DFS, "w", encoding="utf-8") as f:
            json.dump(all_tags_dfs, f, indent=4, ensure_ascii=False)
        logger.info(f"📂 Hasil ekstraksi DFS disimpan: {JSON_DFS} ({len(all_tags_dfs)} jurnal)")

    if all_tags_bfs:
        with open(JSON_BFS, "w", encoding="utf-8") as f:
            json.dump(all_tags_bfs, f, indent=4, ensure_ascii=False)
        logger.info(f"📂 Hasil ekstraksi BFS disimpan: {JSON_BFS} ({len(all_tags_bfs)} jurnal)")

    # Validasi hasil akhir
    if len(all_tags_dfs) == len(all_tags_bfs) == total_journals:
        logger.info("✅ Validasi jumlah data berhasil: Semua data telah diproses.")
    else:
        logger.warning("⚠️ Peringatan: Ada perbedaan jumlah data yang diproses!")

    logger.info("=" * 80)
    logger.info("🎯 Proses ekstraksi selesai! Hasil disimpan di '4_preprocess_scraped_data/'.")
    print("Proses selesai. Cek folder '4_preprocess_scraped_data/' untuk hasil dan log.")
