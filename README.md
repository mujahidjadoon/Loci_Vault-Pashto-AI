 
 Local Pashto AI Assistant
A privacy-first AI assistant for Pashto. Ask questions about your own documents — books, notes, PDFs — by text or voice. Everything runs locally. Nothing leaves your machine.

Why
Pashto is spoken by around 60 million people, but most AI tools handle it poorly or not at all. Cloud APIs aren't always an option for sensitive documents either. This project is one attempt at filling that gap with a fully local stack.

What it does
Ingests Pashto documents and indexes them as vector embeddings
Answers questions by retrieving relevant passages and grounding the response in them (RAG)
Accepts voice input in Pashto via local Whisper
Runs entirely offline — no API keys, no cloud calls
Stack
Component	Tool
LLM runtime	Ollama (Llama 3, Phi-3)
Speech-to-text	Whisper (local)
Vector store	FAISS (ChromaDB optional)
Inference	MLX / PyTorch
Language	Python 3.11+
Built and tested on Apple Silicon (M1, M4).

How it works
Documents get chunked and embedded into a FAISS index. At query time, the question is embedded, the closest chunks are retrieved, and Ollama generates an answer grounded in that retrieved context. Standard RAG pipeline, nothing exotic.

Install

bash
git clone https://github.com/mujahidjadoon/Loci_Vault-Pashto-AI.git
cd Loci_Vault-Pashto-AI

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/main.py
Repository

src/        # RAG pipeline and STT logic
scripts/    # Data preprocessing
docs/       # Documentation
Modelfile   # Model configuration
Use cases
Pashto document Q&A, offline assistants, academic research, language preservation work.

Limitations
Quality depends on the Pashto data you feed it
Speech recognition accuracy varies with audio quality and dialect
RAG reduces hallucinations but doesn't eliminate them
