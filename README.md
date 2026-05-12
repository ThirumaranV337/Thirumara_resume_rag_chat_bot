# 🚀 Thirumaran Resume RAG Chatbot

An AI-powered Resume RAG (Retrieval-Augmented Generation) Chatbot built using LangChain, ChromaDB, HuggingFace Embeddings, Gemini API, and Gradio.

This project allows users to interact with Thirumaran’s resume using natural language questions.

---

# 📌 Features

- 📄 Load Resume PDFs
- ✂️ Smart Text Chunking
- 🧠 Vector Embedding Generation
- 🗂️ Chroma Vector Database Storage
- 🔍 Semantic Retrieval
- 🤖 AI-Powered Question Answering
- 💬 Gradio Chat Interface
- ⚡ Fast Local RAG Pipeline

---

# 🏗️ Project Architecture

```text
Resume PDF
    ↓
PDF Loader (PyPDFLoader / PyMuPDF)
    ↓
Text Extraction
    ↓
RecursiveCharacterTextSplitter
    ↓
Chunks
    ↓
HuggingFace Embeddings
(all-MiniLM-L6-v2)
    ↓
Chroma Vector Database
    ↓
Retriever
    ↓
Gemini LLM
    ↓
Gradio Chat Interface
```

---

# 📂 Project Structure

```bash
thirumaran-resume-rag-chat-bot/
│
├── knowledge-base/
│   └── resume.pdf
│
├── injection.py
├── rag_engine.py
├── pyproject.toml
├── .env
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Text Embeddings |
| Gemini API | LLM Response Generation |
| Gradio | Frontend Chat UI |
| PyMuPDF | PDF Text Extraction |

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/thirumaran-resume-rag-chat-bot.git

cd thirumaran-resume-rag-chat-bot
```

---

## 2️⃣ Create Virtual Environment

### Using UV

```bash
uv venv
```

Activate Environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
uv sync
```

OR

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API=your_api_key_here
```

---

# 📄 Add Resume PDFs

Place your resume PDFs inside:

```bash
knowledge-base/
```

Example:

```bash
knowledge-base/Thirumaran_Resume.pdf
```

---

# 🧠 Create Vector Database

Run:

```bash
python injection.py
```

This process:

- Loads PDFs
- Extracts text
- Splits into chunks
- Generates embeddings
- Stores vectors into ChromaDB

---

# 🤖 Run the RAG Chatbot

```bash
python rag_engine.py
```

---

# 💬 Example Questions

- What are Thirumaran's AI skills?
- What projects has he built?
- Does he know FastAPI?
- What technologies does he use?
- Tell me about his internships.

---

# 🧩 Core Components

## 📌 Document Loading

```python
loader = DirectoryLoader(
    folder,
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)
```

---

## 📌 Text Splitting

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=200
)
```

---

## 📌 Embedding Model

```python
HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
```

---

## 📌 Vector Database

```python
Chroma.from_documents()
```

---

## 📌 Retriever

```python
retriever = vectorstore.as_retriever()
```

---

## 📌 LLM Integration

```python
ChatOpenAI(
    model_name="gemini-3.1-flash-lite"
)
```

---

# 🖥️ Gradio Interface

```python
gr.ChatInterface(
    fn=answer,
    title="🤖 Thirumaran Resume AI Assistant"
)
```

---

# 📊 Dependencies

Main Libraries Used:

```toml
langchain
langchain-chroma
langchain-community
langchain-openai
langchain-huggingface
gradio
sentence-transformers
chromadb
pymupdf
python-dotenv
```

---

# 🚀 Future Improvements

- Multi-PDF Support
- Hybrid Search
- Streaming Responses
- Source Citation
- FastAPI Backend
- Cloud Deployment
- Memory Chat History
- Resume Upload Feature
- Analytics Dashboard

---

# 🛠️ Commands Summary

## Create Vector Database

```bash
python injection.py
```

## Run Chatbot

```bash
python rag_engine.py
```

---

# 📸 Sample Output

```text
User:
What AI skills does Thirumaran have?

Bot:
Thirumaran has experience in:
- Machine Learning
- Generative AI
- LangChain
- RAG Systems
- FastAPI
- Vector Databases
- LLM Integration
```

---

# 📚 Learning Concepts Used

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Embedding Models
- Semantic Search
- Vector Databases
- LLM Integration
- Prompt Engineering
- AI Chatbot Development

---

# 👨‍💻 Author

## Thirumaran

AI & Data Science Student

Passionate about:

- Generative AI
- LLM Applications
- FastAPI
- AI Automation
- RAG Systems
- Open Source Development

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.