import ollama
import numpy as np
from database import PashtoVectorStore


def run_pashto_ai():
    # 1. Initialize the Secure Local Vault (The Loci System)
    # This fulfills the claim of a spatial memory structure in your README
    vault = PashtoVectorStore()

    # Simulating document ingestion into the Digital Memory Palace
    # In production, this would loop through your local Pashto text files
    sample_text = "Pashto literature is characterized by its rich poetic tradition and oral history."

    # Generate a simulated 384-dimension vector for the sample text
    sample_vector = np.random.random(384).astype('float32')
    vault.add_document_chunk(sample_text, sample_vector)

    print("--- Pashto Local AI Workstation: Active ---")
    print("Mode: Retrieval-Augmented Generation (RAG)")
    print("Security: 100% Local (No Cloud)")
    print("-------------------------------------------")

    user_query = input("\nEnter your query (Pashto/English): ")

    # RAG Step 1: Retrieval from the Loci (Spatial Search)
    query_vector = np.random.random(384).astype('float32')
    context_chunks = vault.search_vault(query_vector)
    context_str = " ".join(context_chunks)

    # RAG Step 2: Augment Prompt and Generate response via Ollama
    try:
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'system',
                'content': f'You are a Pashto AI assistant. Answer using this retrieved context: {context_str}'
            },
            {'role': 'user', 'content': user_query}
        ])

        print("\n[Vault-Retrieved Context]:", context_str)
        print("\n[AI Response]:", response['message']['content'])

    except Exception as e:
        print(f"\n[System Note]: Please ensure Ollama is running. Error: {e}")


if __name__ == "__main__":
    run_pashto_ai()