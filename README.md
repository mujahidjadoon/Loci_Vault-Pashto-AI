🛡️ LociVault: Privacy-First Local Pashto AI Assistant
🚀 Overview

LociVault is a privacy-first AI framework designed for low-resource languages such as Pashto. It enables users to build a local, context-aware question-answering system over their own documents without relying on cloud services.

The system is based on Retrieval-Augmented Generation (RAG), where user-provided Pashto texts are indexed using vector embeddings and retrieved at query time to generate grounded responses.

All components run locally on Apple Silicon devices, ensuring full data privacy and offline usability.

✨ Core Features:

📚 Context-Aware Document Retrieval

Ingests Pashto documents (books, notes, PDFs)
Converts text into embeddings
Retrieves relevant content using similarity search
Improves answer relevance by grounding responses in retrieved context

🎙️ Speech-to-Text Support

Uses OpenAI Whisper for Pashto speech recognition
Converts spoken input into text queries
Accuracy depends on audio quality and dialect

🔒 Fully Local & Private

Runs locally via Ollama
Uses FAISS for vector search
Optional support for ChromaDB
No external API calls required

🍎 Apple Silicon Support

Efficient execution on Apple M-series (M1–M4) devices
Supports MLX / PyTorch-based inference
Optimized for local workloads

🧠 System Architecture

The system follows a standard RAG pipeline:

1. Document Ingestion
 
.....Text is split into chunks

.....Each chunk is converted into embeddings

2. Vector Storage

.....Embeddings are stored in a FAISS index

.....Original text is stored in metadata

3. Query Processing

.....User query is converted into embeddings

.....Similar chunks are retrieved using vector similarity

4. Response Generation

.....Retrieved context is passed to the LLM

.....Ollama generates the final response
   
🛠️ Technical Stack

Component	             Technology
LLM Runtime	     Ollama (Llama 3, Phi-3)
Speech-to-Text	  OpenAI Whisper (Local)
Vector Database	         FAISS
Optional Database	       ChromaDB
Inference Engine	       MLX / PyTorch
Language	                Python 3.11+

📂 Repository Structure

src/        # Core RAG pipeline and STT logic  
scripts/    # Data preprocessing  
docs/       # Documentation  
Modelfile/  # Model configuration  

⚙️ Installation

git clone https://github.com/mujahidjadoon/Loci_Vault-Pashto-AI.git
cd Loci_Vault-Pashto-AI

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python src/main.py

🎯 Use Cases

Pashto document question answering
Offline AI assistant
Academic research support
Language preservation

⚠️ Limitations

Performance depends on available Pashto datasets
Speech recognition accuracy may vary
RAG reduces hallucinations but does not eliminate them

💡 Design Note


The name “LociVault” is inspired by the Method of Loci (Memory Palace) concept.
However, the current implementation uses vector-based semantic retrieval rather than explicit spatial memory modeling.
