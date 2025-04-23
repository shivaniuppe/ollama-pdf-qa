## ✅ `README.md`

```markdown
# 🧠 PDF Q&A Chatbot with Ollama

This is a lightweight Flask-based web application that allows users to upload a PDF and ask questions about its content. It uses a locally hosted LLM (e.g., LLaMA 3 via Ollama) to generate answers, simulating a Retrieval-Augmented Generation (RAG)-like system.

---

## 🚀 Features

- 📄 PDF upload and text extraction (via PyMuPDF)
- 💬 Natural language Q&A powered by Ollama and `llama3.2`
- ⚡ Local, fast, and private (no cloud LLM required)
- 🎨 Styled HTML frontend with custom form and result display
- 🔁 Ready for integration with vector search or real RAG pipelines

---

## 🛠️ Tech Stack

- **Frontend**: HTML/CSS (templated via Flask)
- **Backend**: Python Flask
- **LLM Engine**: [Ollama](https://ollama.com/) running `llama3.2`
- **PDF Parsing**: PyMuPDF (`fitz`)
- **HTTP Client**: `requests`

---

## 🧪 How It Works

1. User uploads a PDF and types a question
2. The app extracts text (limited to the first 3000 characters for simplicity)
3. The question + extracted content is sent as a prompt to Ollama
4. Ollama returns a context-aware answer
5. The answer is displayed on the same page

---

## 🧰 Getting Started

### 1. Install Dependencies

Make sure Python 3 is installed.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Install & Run Ollama

[Download Ollama](https://ollama.com/download) and run:

```bash
ollama pull llama3.2
ollama run llama3.2
```

### 3. Run the App

```bash
python3 app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
ollama-pdf-qa/
├── app.py
├── uploads/                # Uploaded PDF files
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── README.md
├── .gitignore
```

---

## ✅ Example Question

> 🔍 **PDF:** Building Safety Report  
> 💬 **Question:** What fire safety measures are required in the building?

🧠 **Answer (from LLM):**  
The building requires illuminated signage for exit routes, two stairwells for emergency evacuation, smoke detectors on all floors, and a sprinkler system in all enclosed rooms.

---

## 📌 Notes

- This is not a true RAG pipeline (no vector store). It's a simple demo using a prompt that includes extracted PDF text.
- You can easily extend it to use LangChain, FAISS/Chroma, or a cloud-hosted model like GPT or Claude.

---

## 📃 License

MIT – free to use, modify, or build upon.

---

## 👩‍💻 Author

**Shivani Uppe**  
Master of Applied Computer Science – Dalhousie University  
[LinkedIn](https://www.linkedin.com/in/shivaniuppe) | [GitHub](https://github.com/shivaniuppe)
