import requests  # Ye library internet/local connection ke liye hai
import json  # Ye data ko sahi format mein badalne ke liye hai


def ask_local_ai(prompt):
    """
    Ye function aapke sawal ko Ollama tak le kar jayega.
    """
    url = "http://localhost:11434/api/generate"

    # Ye wo saaman hai jo hum AI ko bhej rahe hain
    data = {
        "model": "llama3:8b",  # Aapka main intelligent model
        "prompt": prompt,  # Aapka sawal
        "stream": False  # Hum chahte hain pura jawab ek saath aaye
    }

    try:
        # AI ko request bhejna
        response = requests.post(url, json=data)

        # AI se jawab wapis lena
        result = response.json()
        return result['response']

    except Exception as e:
        return f"Error: Shayad Ollama band hai. Pehle Ollama App kholien! {str(e)}"


# --- YAHAN SE AAP APNA SAWAL POOCH SAKTE HAIN ---
if __name__ == "__main__":
    print("AI se rabta ho raha hai...")

    sawal = "Pashto mein 'How are you' kaise kehte hain?"
    jawab = ask_local_ai(sawal)

    print("-" * 30)
    print(f"Sawal: {sawal}")
    print(f"AI Jawab: {jawab}")
    print("-" * 30)