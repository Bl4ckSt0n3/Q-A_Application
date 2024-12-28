from wtforms import FileField, SubmitField
from flask_wtf import FlaskForm

class FileUploadForm(FlaskForm):
    file = FileField("PDF_File")
    submit = SubmitField("Save File")