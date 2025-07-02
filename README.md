# 🧠 AI-Powered MCQ Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey?logo=flask)
![spaCy](https://img.shields.io/badge/spaCy-3.8-green?logo=spacy)
[![Deploy to Render](https://img.shields.io/badge/Deployed%20Live-On%20Render-brightgreen)](https://mcq-gen-phin.onrender.com)

This is a web application that uses NLP to dynamically generate multiple-choice questions (MCQs) from user-uploaded **PDFs or text**. Built with Flask and spaCy, it intelligently extracts key nouns from your content and creates MCQs with distractor options.

---

## 🌐 Live App
👉 [Try it on Render](https://mcq-gen-phin.onrender.com)

---

## 🚀 Features
- 📄 Upload **PDF** or **TXT** files
- ✏️ Or **paste custom text**
- 🔢 Select **1–50 questions**
- 🧠 Uses **spaCy** NLP engine to extract sentence structure and generate questions
- 📊 Tracks progress, % completed, and answer stats
- 👁️ Reveal correct answers at the end

---

## 📁 Project Structure
```
mcq_gen/
├── app.py                  # Flask application logic
├── requirements.txt        # Dependencies
├── static/
│   ├── stylesi.css         # Input page styling
│   └── stylesm.css         # Quiz display styling
├── templates/
│   ├── index.html          # Input/upload form
│   └── mcqs.html           # MCQ output UI
├── .gitignore              # Ignored IDE, venv, cache files
└── README.md
```

---

## ⚙️ Tech Stack
- **Python 3.10+**
- **Flask** (Backend)
- **spaCy** (NLP Engine)
- **PyPDF2** (PDF Parsing)
- **Bootstrap + Font Awesome** (UI)
- **Render** (Hosting)

---

## 📦 Installation
```bash
# 1. Clone the repo
$ git clone https://github.com/Azzanraj/mcq_gen.git
$ cd mcq_gen

# 2. Create virtual environment
$ python -m venv .venv
$ .\.venv\Scripts\activate  # Windows

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Download spaCy model
$ python -m spacy download en_core_web_sm

# 5. Run the app
$ python app.py
```

---

## 🧪 Example Use Cases
- Teachers converting class notes to quizzes
- Students generating practice questions
- Companies creating onboarding assessments

---

## 📄 License
This project is open-source for academic/non-commercial use.

---

## 🙋‍♂️ Author
Built with ❤️ by [@Azzanraj](https://github.com/Azzanraj)
