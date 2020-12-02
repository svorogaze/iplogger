from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return 'ez ip logged lol ' + str(request.environ['REMOTE_ADDR'])
    else:
        return 'ez ip logged lol ' + str(request.environ['HTTP_X_FORWARDED_FOR'])


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
