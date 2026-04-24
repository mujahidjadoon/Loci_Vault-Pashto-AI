from datasets import load_dataset
import os


def download_wikipedia_pashto():
    print("--- Professional Data Ingestion Shuru ---")

    # Directory check
    os.makedirs("data/raw", exist_ok=True)

    try:
        # Aap ke screenshot ke mutabiq sahi subset: "20231101.ps"
        print("Fetching Pashto Wikipedia (Subset: 20231101.ps)...")

        # 'wikimedia/wikipedia' use karenge kyunki ye Parquet format hai
        ds = load_dataset("wikimedia/wikipedia", "20231101.ps", split="train")

        output_path = "data/raw/pashto_corpus.txt"

        # Data ko extraction ke baad text file mein save karna
        print(f"Saving {len(ds)} articles to {output_path}...")

        with open(output_path, "w", encoding="utf-8") as f:
            for i, article in enumerate(ds):
                # Wikipedia mein 'text' field hoti hai
                f.write(article['text'].replace('\n', ' ') + "\n")

                if i % 500 == 0:
                    print(f"Processed {i} articles...")

        print("\n--- MUBARAK HO! Raw Data Tayyar Hai ---")

    except Exception as e:
        print(f"Professional Error Report: {e}")


if __name__ == "__main__":
    download_wikipedia_pashto()