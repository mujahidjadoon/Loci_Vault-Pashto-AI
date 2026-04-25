🛡️ Loci_Vault: Privacy-First Local Pashto AI Assistant

🚀 Overview

Loci_Vault is a specialized AI framework designed to solve the data scarcity and privacy challenges in low-resource languages like Pashto. 
By integrating the Method of Loci (Spatial Memory) with Retrieval-Augmented Generation (RAG), the system creates a "Digital Memory Palace" where your documents are spatially indexed for hyper-accurate retrieval. 
Running 100% locally on the Apple M4 Silicon, it acts as a secure, offline vault that transforms static Pashto literature into a private, context-aware intelligence base.

✨ Core Features

📚 Intelligent Context-Aware RAG
Unlike standard LLMs that rely solely on pre-trained data, Loci_Vault can ingest specific Pashto books and documents. It extracts precise answers from the provided context, 
making it significantly more reliable for academic or professional use where accuracy is critical.

🎙️ Advanced Pashto Speech-to-Text (STT)
Integrated with OpenAI's Whisper, optimized for Pashto phonetics to ensure seamless transition from voice commands to digital text.

🍎 M4 Silicon Optimization
Leveraging the Unified Memory Architecture of Apple's latest chip, the system manages large vector embeddings and LLM weights with extreme efficiency.

🔒 Zero-Cloud Dependency
Operating via Ollama, the system is 100% offline. No data is ever sent to external servers, making it ideal for sensitive Pashto linguistic research.



📸 Project Showcase (Evolution of Logic)

1️⃣ General Pashto Discussion
Initial interaction showing the model's base understanding of Pashto linguistics and conversational flow.

2️⃣ Context Injection (Book Loading)
Demonstrating the process of adding specific Pashto literature/books into the local vector database.

3️⃣ Contextual Question Answering
Once the book is indexed, the model provides 100% accurate answers based only on the provided text, eliminating hallucinations.

4️⃣ Deep Knowledge Extraction
Showcasing the system's intelligence in understanding complex queries within the Pashto context.

🛠️ Technical Stack

Component                  Technology
LLM Infrastructure    Ollama (Llama-3, Phi-3)"
STT Engine               OpenAI Whisper
Inference Engine    Apple MLX / PyTorch (M4 Optimized)
Vector Storage      Local FAISS / ChromaDB for RAG


Installation & Setup
Clone & Navigate:
Bash
git clone https://github.com/mujahidjadoon/Loci_Vault-Pashto-AI.git
cd Loci_Vault-Pashto-AI


Virtual Environment:
Bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Run Application:
Bash
python src/main.py


📂 Repository Structure
src/: Core logic for RAG and Pashto STT processing.

scripts/: Data cleaning scripts for limited Pashto datasets.

docs/: Technical documentation and system architecture.

🤝 Contributing
We are focused on improving Pashto NLP accuracy. Feel free to open issues or submit pull requests to enhance the local Pashto intelligence.











