import flask
from helper import score

app = flask.Flask(__name__)

@app.route("/")
def index():
    keeper = score.Score()
    highscore = keeper.high_score()
    return flask.render_template("index.html", highscore=highscore)

@app.route("/scores")
def scores():
    keeper = score.Score()
    scores = keeper.sorter()
    return flask.render_template("scores.html", scores=scores)


@app.route("/scores/<string:name>")
def player(name):
    keeper = score.Score()
    player = keeper.get_score(name)
    return flask.render_template("player.html", player=player)

@app.route("/game")
def game():
    return flask.render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)