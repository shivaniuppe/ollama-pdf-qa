from flask import Flask, render_template, request, jsonify
import fitz  # PyMuPDF
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text[:3000]  

def ask_ollama(question, context):
    prompt = f"""
You are a building safety assistant. Use only the provided document text to answer the question.

Document Text:
{context}

Question: {question}

Answer in clear, complete sentences based on the document above.
"""

    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={"model": "llama3.2", "prompt": prompt, "stream": False}
        )
        response_json = response.json()
        print("💬 Ollama API Response:", response_json)

        return response_json.get("response", "⚠️ No answer returned from the model.")

    except Exception as e:
        print("🔥 Error calling Ollama:", e)
        return "⚠️ Something went wrong while getting the response from Ollama."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf']
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        question = request.form['question']
        context = extract_text_from_pdf(file_path)
        answer = ask_ollama(question, context)
        return render_template('index.html', answer=answer)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
