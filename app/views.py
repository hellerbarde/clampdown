import flask
from app import app


@app.route('/')
def index():
    return flask.render_template('index.html', action="")


@app.route('/control/<action>')
def control(action):
	actions = ["prev", "play", "pause", "stop", "next"]
	if action not in actions: 
		flask.abort()
	return flask.render_template("index.html", action=action)


@app.errorhandler(404)
def internal_error(error):
    return flask.render_template('404.html'), 404
