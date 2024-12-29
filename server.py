from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "HEY !!!! Welcome to the flask-kubctl server from 87228"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7001,debug=True)
