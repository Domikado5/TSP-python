from flask import Flask, render_template
import flask_socketio
import os

app = Flask(__name__)

@app.route('/')
def index():
    dataInput = [file for file in os.listdir("./data") if file.endswith(".txt")]
    algorithms = [[0, "greedy"], [1, "ant-colony"]]
    return render_template('index.html', dataInput=dataInput, algorithms=algorithms)