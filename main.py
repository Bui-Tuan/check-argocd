from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World and hello cong! \n it all right! 10:20'


@app.route('/health')
def health():
    return 'OK! Done!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
