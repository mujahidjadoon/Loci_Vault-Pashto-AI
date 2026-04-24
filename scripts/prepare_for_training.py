import json
import random
import os

def prepare():
    input_file = "data/processed/pashto_clean.txt"
    output_dir = "data/training_data"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Data ko shuffle karna taake sequence ka bias na rahe
    random.shuffle(lines)
    
    # Split: 90% Train, 10% Validation
    split_idx = int(len(lines) * 0.9)
    train_lines = lines[:split_idx]
    valid_lines = lines[split_idx:]
    
    def save_jsonl(data, filename):
        path = os.path.join(output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            for line in data:
                # LLM training format: {"text": "Aapki line yahan"}
                json.dump({"text": line.strip()}, f, ensure_ascii=False)
                f.write("\n")
        return path

    train_path = save_jsonl(train_lines, "train.jsonl")
    valid_path = save_jsonl(valid_lines, "valid.jsonl")
    
    print(f"--- Training Data Tayyar Hai ---")
    print(f"Train samples: {len(train_lines)} -> {train_path}")
    print(f"Valid samples: {len(valid_lines)} -> {valid_path}")

if __name__ == "__main__":
    prepare()
