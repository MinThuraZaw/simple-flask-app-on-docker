from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

todos = []


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
