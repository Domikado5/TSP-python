from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
import main
import greedy
import ploter as pl
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
socketio = SocketIO(app)

socketio.run(app)

@socketio.on('my event')
def handle_connect(json):
    print(json['data'])

@socketio.on('calculate')
def calculate(json):
    print("Recieved calculate request")
    if json['input'] in ['./data/berlin52.txt', './data/bier127.txt', './data/input.txt', './data/tsp250.txt', './data/tsp500.txt', './data/tsp1000.txt']:
        if int(json['alg']) in [0, 1]:
            cities = main.Load(filename=json['input'])
            if int(json['alg']) == 0:
                distance, path, coordinates = greedy.main(cities)
            else:
                distance, path, coordinates = greedy.main(cities) # change it later to ant colony!!!!!
            main.PathToFile(path)
            pl.generateInteractiveGraph(x=coordinates[0], y=coordinates[1])
            data = {
                "distance": distance
            }
            emit('calculated', data)

@socketio.on('generate')
def generate(json):
    print("Recieved generate request")
    if int(json['size']) >= 0 and int(json['size']) < 1000:
        if int(json['alg']) in [0, 1]:
            cities = main.Generate(size=int(json['size']))
            if int(json['alg']) == 0:
                distance, path, coordinates = greedy.main(cities)
            else:
                distance, path, coordinates = greedy.main(cities) # change it later to ant colony!!!!!
            main.PathToFile(path)
            pl.generateInteractiveGraph(x=coordinates[0], y=coordinates[1])
            data = {
                "distance": distance
            }
            emit('generated', data)

@app.route('/')
def index():
    dataInput = [file for file in os.listdir("./data") if file.endswith(".txt")]
    algorithms = [[0, "greedy"], [1, "ant-colony"]]
    return render_template('index.html', dataInput=dataInput, algorithms=algorithms)