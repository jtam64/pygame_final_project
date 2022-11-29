import flask
from helper import score

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    '''Render the homepage of the webpage
    '''
    if flask.request.method == "GET":
        keeper = score.Score()
        highscore = keeper.high_score()
        return flask.render_template("index.html", highscore=highscore)

    if flask.request.method == "POST":
        text = flask.request.form["text"].upper()
        return flask.redirect(flask.url_for("player", name=text))


@app.route("/scores", methods=["GET", "POST"])
def scores():
    '''Render the scores page of the webpage
    '''
    keeper = score.Score()
    if flask.request.method == "GET":
        scores = keeper.sorter()
        return flask.render_template("scores.html", scores=scores)

    if flask.request.method == "POST":
        value = flask.request.form["sortby"]
        scores = keeper.sorter(value)
        return flask.render_template("scores.html", scores=scores)


@app.route("/scores/<string:name>", methods=["GET"])
def player(name:str):
    '''Render all the scores for an individual player
    '''
    keeper = score.Score()
    try:
        scores = keeper.get_score(name)
        return flask.render_template("player.html", scores=scores, name=name)
    except (KeyError):
        return flask.redirect(flask.url_for("scores"))

@app.route("/game", methods=["GET"])
def game():
    '''Render the game page for downloads
    '''
    return flask.render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)