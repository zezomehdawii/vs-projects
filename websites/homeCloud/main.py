from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('index.html', form=form) 

# @app.route('/files')
# def get_files():
#     folderPath = r"D:\\vs projects\\websites\\homeCloud\\files"
#     files = os.listdir(folderPath)
#     print (files)
#     return render_template('files.html', files=files)
path = r"d:\\vs projects\\websites\\homeCloud\\files" 

@app.route('/files', defaults={'req_path': ''})
@app.route('/files:\\vs projects\\websites\\homeCloud\\files>')
def dir_listing(req_path):
    global RENDER_OUTPUT_DIR
    BASE_DIR = RENDER_OUTPUT_DIR
    abs_path = os.path.join(BASE_DIR, req_path)
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)


if __name__ == '__main__':
    app.run(debug=True)