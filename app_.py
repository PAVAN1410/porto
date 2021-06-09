
from flask import Flask, render_template, url_for, request, send_file
from app import *
import linkedin_scrapper
import zip_req

app = Flask(__name__, template_folder='rendering')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index_.html')


@app.route('/build_porto')
def build_porto():
    return render_template('build_porto.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        linkedin_scrapper.scrapper(result['URL'])
        print(result['URL'])
        zip_req.zipit()
        return render_template("messagescreen.html")
        # return render_template("index.html")

@app.route('/get_things')
def get_things():
    return render_template("get_things.html")

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route('/download')
def download_file():
    p = "webzip.zip"
    return send_file(p,as_attachment=True)


@app.route('/help/')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)
