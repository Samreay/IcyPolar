#!flask/bin/python
from flask import Flask, send_file


app = Flask(__name__)

@app.route("/antarctica")
def antartica():
    return send_file("templates/antartica.html")

@app.route("/glacier")
def glacier():
    return send_file("templates/glacier.html")

@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route('/search/<string:phrase>', methods=['GET'])
def do_search(phrase):
    print("Server has search request for %s" % phrase)
    return "You searched for %s" % phrase

if __name__ == '__main__':
    app.run(debug=True)