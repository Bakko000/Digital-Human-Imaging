
import os
import subprocess
import json
from flask import Flask, render_template, request, redirect, url_for, abort, session
from werkzeug.utils import secure_filename
from flask_cors import CORS # Da disabilitare in un'eventuale deploy per ragioni di sicurezza


app = Flask(__name__)
CORS(app, resources = r'/static/example/DSTresults/*')    # Da disabilitare in un'eventuale deploy per ragioni di sicurezza
app.secret_key = 'dighum' #the secret_key can be anything
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg']   # estensioni accettate 
app.config['UPLOAD_PATH'] = 'venv/DST/example'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content', methods=['POST'])
def upload_content():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        new_filename = "{}{}".format("content", file_ext)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], new_filename))
    return redirect(url_for('index'))

@app.route('/style', methods=['POST'])
def upload_style():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        new_filename = "{}{}".format("style", file_ext)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], new_filename))
    return redirect(url_for('index'))


@app.route('/nst')
def nst():
    maxiter = session.get('iter', None)
    contentw = session.get('content_w', None)
    regw = session.get('reg_w', None)
    subprocess.Popen([r'%USERPROFILE%\myproject\venv\NST.bat', str(maxiter), str(contentw), str(regw)], shell=True)
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output) #this converts the json output to a python dictionary
    session['iter'] = result['iter']
    session['content_w'] = result['content_w']
    session['reg_w'] = result['reg_w']
    return result


## Codici per le altre pagine del sito web #

@app.route('/comefunziona')
def comefunziona():
    return render_template('comefunziona.html')

@app.route('/casi')
def casi():
    return render_template('casi.html')


if __name__ == "__main__":
    app.run(debug=True)

