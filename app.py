from flask import Flask
app = Flask(__name__)
import os

@app.route('/')
def hello_world():
    stream = os.popen('pagedjs-cli mp.html')
    output = stream.read()
    # might need to use lambda. v2
    return f'<h1>pagedjs output</h1> {output}'