from flask import Flask
app = Flask(__name__)
import os

@app.route('/')
def hello_world():
    stream = os.popen('echo Returned output')
    output = stream.read()

    return f'Hello, World!\n\n {output}'