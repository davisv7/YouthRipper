from flask import Flask, render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField

from meat import download

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'stuff'
app.config['UPLOAD_FOLDER'] = 'albumzips/'


@app.route('/', methods=['GET', 'POST'])
def divide():
    class UrlLink(FlaskForm):
        webLink = StringField("Album Name:")

    form = UrlLink()
    result = None

    if form.validate_on_submit():
        result = download(form.webLink.data)

    return render_template('divide.html', result=result, form=form)


@app.route('/albumzips/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000)
