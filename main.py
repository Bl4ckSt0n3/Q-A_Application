from openai import OpenAI
from transformers import pipeline
import PyPDF2
from flask import Flask, render_template, request, jsonify, redirect
from FormFields.File_Upload_Form_Field import FileUploadForm
from FormFields.Question_Form_Field import QuestionForm
from werkzeug.utils import secure_filename
import os


# generate flask app
app = Flask(__name__)

app.config['UPLOAD_FOLDER']='static/files'

# index page
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_upload_form = FileUploadForm()

    if file_upload_form.validate_on_submit():
        file = file_upload_form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_content = extract_text_from_pdf_file(file_path)
        print("file name: " + filename)
        print("content: " + file_content)
        return redirect('/form', 302)
    return render_template('question_form.html', file_upload_form=file_upload_form)

# q&a form
@app.route('/form', methods=['GET', 'POST'])
def index_page():
    question_form = QuestionForm()

    if question_form.validate_on_submit():
        question = question_form.question.data
        print("question: " + question)
    return render_template('qa_form.html', question_form=question_form)

# # Q&A pipeline
# qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# # function helps to extract text from pdf 
def extract_text_from_pdf_file(file_path) -> str:
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = "".join(page.extract_text())
    return text

# pdf_content = extract_text_from_pdf_file("./file/qa_pdf.pdf")
# print(pdf_content)



# text = """
#     this text includes information about supersport cars. the best car is ferrari and the second is ford.
# """

# question = str(input("question: "))
# result = qa_pipeline({
#     'context': text,
#     'question': question # 'what is the best car?'
# })

# print(result)


if __name__ == "__main__":
    # flask --app main --debug run
    app.run(debug=True)