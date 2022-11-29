import flask
from helper import score

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    keeper = score.Score()
    highscore = keeper.high_score()
    return flask.render_template("index.html", highscore=highscore)

@app.route("/scores", methods=["GET"])
def scores(name=None):
    keeper = score.Score()
    scores = keeper.sorter()
    return flask.render_template("scores.html", scores=scores)


@app.route("/scores/<string:name>", methods=["GET"])
def player(name):
    keeper = score.Score()
    try:
        scores = keeper.get_score(name)
        return flask.render_template("player.html", scores=scores, name=name)
    except (KeyError):
        return flask.redirect(flask.url_for("scores", name=name))


@app.route("/", methods=["POST"])
def search():
    text = flask.request.form["text"].upper()
    return flask.redirect(flask.url_for("player", name=text))


@app.route("/game", methods=["GET"])
def game():
    return flask.render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)