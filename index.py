from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'WEB App di Ludovico Grasso'

@app.route('/start')
def hello():
    return 'Inizio WEB APP'