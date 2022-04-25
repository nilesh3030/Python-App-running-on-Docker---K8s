import os, pandas as pd
from flask import Flask, render_template, url_for,request
from werkzeug.utils import secure_filename

app = Flask(__name__)

posts = "Welcome to My App"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/upload",methods = ['GET','POST'])
def upload():
    return render_template('upload.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        global f
        global data_file
        global word_count
        f = request.files['file']
        f.save(secure_filename(f.filename))
        f = open(f.filename)
        word_list = f.read().split()
        word_count = len(word_list)
        return render_template('result.html', word_count = word_count)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)