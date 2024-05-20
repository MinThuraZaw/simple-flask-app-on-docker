from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home')
def welcome():
    return render_template('home.html')


@app.route('/redirect_to_home', methods=['POST'])
def redirect_to_welcome():
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
