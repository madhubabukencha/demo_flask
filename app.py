from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<h1>My First Flask App</h1>"

@app.route("/wishme")
def wishme():
    return "<h1>Hello Madhu, Welcome to Flask</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug = True)
