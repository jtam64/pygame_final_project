import flask
from game.helper import score

app = flask.Flask(__name__)

@app.route("/")
def index():
    keeper = score.Score()
    return flask.render_template("index.html", keeper=keeper)

if __name__ == "__main__":
    app.run(debug=True)