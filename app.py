import flask
from helper import score

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        keeper = score.Score()
        highscore = keeper.high_score()
        return flask.render_template("index.html", highscore=highscore)

    if flask.request.method == "POST":
        text = flask.request.form["text"].upper()
        return flask.redirect(flask.url_for("player", name=text))


@app.route("/scores", methods=["GET", "POST"])
def scores(value:str="Score"):
    keeper = score.Score()

    if flask.request.method == "GET":
        print(value)
        scores = keeper.sorter(value)
        return flask.render_template("scores.html", scores=scores)

    if flask.request.method == "POST":
        value = flask.request.form["sortby"]
        print(value)
        return flask.redirect(flask.url_for("scores", value=value))


@app.route("/scores/<string:name>", methods=["GET"])
def player(name:str):
    keeper = score.Score()
    try:
        scores = keeper.get_score(name)
        return flask.render_template("player.html", scores=scores, name=name)
    except (KeyError):
        return flask.redirect(flask.url_for("scores"))

@app.route("/game", methods=["GET"])
def game():
    return flask.render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)