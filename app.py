from flask import Flask
app = Flask(__name__)
import os

@app.route('/')
def hello_world():
    stream = os.popen('pagedjs-cli mp.html')
    output = stream.read()

    return f'<h1>pagedjs output</h1> {output}'