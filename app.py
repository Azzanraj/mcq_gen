from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import spacy
from collections import Counter
import random
from PyPDF2 import PdfReader

app = Flask(__name__)
Bootstrap(app)
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    content = ""
    pdf = PdfReader(file)
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            content += page_text
    return content

def create_mcqs(text, total=5):
    if not text.strip():
        return []

    doc = nlp(text)
    all_sentences = list(doc.sents)
    total = min(total, len(all_sentences))

    chosen_sentences = random.sample(all_sentences, total)
    questions = []

    for sent in chosen_sentences:
        tokens = [token.text for token in sent if token.pos_ == "NOUN"]
        if len(tokens) < 2:
            continue

        main_word = Counter(tokens).most_common(1)[0][0]
        question = sent.text.replace(main_word, "_____")
        options = list(set(tokens) - {main_word})
        while len(options) < 3:
            options.append("[Option]")
        distractors = random.sample(options, 3)
        all_choices = [main_word] + distractors
        random.shuffle(all_choices)
        correct = chr(65 + all_choices.index(main_word))
        questions.append((question, all_choices, correct))

    return questions

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = ""

        # Check uploaded files
        if request.files.getlist('files[]'):
            for f in request.files.getlist('files[]'):
                if f.filename.endswith('.pdf'):
                    data += extract_text_from_pdf(f)
                elif f.filename.endswith('.txt'):
                    data += f.read().decode('utf-8')

        # Fallback to pasted text
        if not data.strip():
            data = request.form.get('text', '')

        try:
            num = int(request.form.get('num_questions', 5))
            num = min(max(num, 1), 50)
        except:
            num = 5

        mcqs = create_mcqs(data, total=num)
        indexed_mcqs = [(i + 1, q) for i, q in enumerate(mcqs)]
        return render_template("mcqs.html", mcqs=indexed_mcqs)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
