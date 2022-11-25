import flask
from helper import score

app = flask.Flask(__name__)

@app.route("/")
def index():
    keeper = score.Score()
    return flask.render_template("index.html", keeper=keeper)

@app.route("/scores")
def scores():
    keeper = score.Score()
    return flask.render_template("scores.html", keeper=keeper)


@app.route("/scores/<string:name>")
def player(name):
    
    return flask.render_template("player.html")

@app.route("/game")
def game():
    return flask.render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)