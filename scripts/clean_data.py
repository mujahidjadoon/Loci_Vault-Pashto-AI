import json


def filter_data():
    input_file = "data/youtube_text/train.jsonl"
    output_file = "data/youtube_text/train_clean.jsonl"

    clean_lines = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            text = data["text"]
            # Agar aik hi lafz 3 se zyada baar repeat ho raha ho, toh line delete kar do
            words = text.split()
            if len(set(words)) / len(words) < 0.4:  # Repetition check
                continue
            clean_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(clean_lines)
    print(f"Done! Cleaned data saved. Original: {len(clean_lines)}")


filter_data()