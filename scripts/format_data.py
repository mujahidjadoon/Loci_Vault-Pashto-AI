import json
import os


def clean_and_format():
    input_file = "../src/data/youtube_text/pashto_chat.txt"
    output_file = "data/youtube_text/train_data.jsonl"

    if not os.path.exists(input_file):
        print("Error: pashto_chat.txt nahi mili!")
        return

    print("Cleaning and formatting data...")

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Hum 20-20 lines ke blocks banayenge taake model ko lambi baat samajh aaye
    with open(output_file, "w", encoding="utf-8") as f_out:
        for i in range(0, len(lines), 20):
            context = "".join(lines[i:i + 10]).strip()  # Pehli 10 lines as Context
            response = "".join(lines[i + 10:i + 20]).strip()  # Agli 10 lines as Response

            if context and response:
                # Gemma ka khas format
                entry = {
                    "text": f"<|user|>\n{context}\n<|assistant|>\n{response}"
                }
                f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Success! {output_file} tayyar hai training ke liye.")


if __name__ == "__main__":
    clean_and_format()