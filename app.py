from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# url http://127.0.0.1:5000/f/100.2
@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=0.0):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"

if __name__ == '__main__':
    app.run()
