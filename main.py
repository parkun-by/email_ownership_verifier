import verifier

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'email verifier'


@app.route('/validate')
def validate():
    return verifier.send_verification_mail(request.args)


if __name__ == '__main__':
    app.run(threaded=True)
