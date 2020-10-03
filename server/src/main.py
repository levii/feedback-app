import flask
import common.user.bind  # noqa
from common.user.presentation import register_user_blueprints

app = flask.Flask(__name__)


@app.route('/')
def hello():
    return flask.render_template('index.html')


blueprint = flask.Blueprint(name="blueprint", import_name=__name__)

register_user_blueprints(blueprint)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
