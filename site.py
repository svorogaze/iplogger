import flask

app = flask.Flask(__name__)


@app.route('/')
def iplogger():
    s = flask.request.remote_addr
    return 'ez ip logged lol: ' + s


app.run(host="0.0.0.0", port=8080)