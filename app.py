from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def index():
    return 'ez ip logged lol: ' + str(request.environ.get('REMOTE_ADDR', request.remote_addr))


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
