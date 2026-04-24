from datasets import load_dataset

print("🚀 Pashto Data loading shuru... (Cache se utha raha hai)")

try:
    # 1. Dataset ko load karein (Ye ab foran ho jayenge kyunke cache mein hai)
    dataset = load_dataset("saillab/alpaca-pashto-cleaned", split="train")

    # 2. File likhna shuru karein
    file_name = "Pashto_Training_Data.txt"
    print(f"📄 Data ko {file_name} mein save kar raha hoon...")

    with open(file_name, "w", encoding="utf-8") as f:
        # Sirf pehle 2000 items uthatay hain taake process fast ho
        limit = min(2000, len(dataset))
        for i in range(limit):
            instruction = dataset[i].get('instruction', '')
            output = dataset[i].get('output', '')
            f.write(f"Sawal: {instruction}\nJawab: {output}\n\n")

    print(f"✅ Mubarak ho! {file_name} project folder mein ban gayi hai.")

except Exception as e:
    print(f"⚠️ Error aaya hai: {str(e)}")