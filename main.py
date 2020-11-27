import numpy as np
import random as rn
from numpy import version
import greedy as gd
import ploter as pl

from numpy.core.multiarray import result_type

def Generate(size=False, matrix=None):
    vertices = []

    while True and type(size) != int:
        size = input("Please type how many cities to generate: ")
        try:
            size = int(size)
        except:
            print("Please type a number!")
        finally:
            break

    if matrix is None:
        matrix = size*10

    for i in range(size):
        while True:
            x = rn.randint(0, matrix)
            y = rn.randint(0, matrix)
            if [x,y] not in vertices:
                vertices.append([x,y])
                break
    Save(size=size, data=vertices)
    vertices = np.array(vertices)

    return vertices

def Save(filename='./data/input.txt', size=0, data=[]):
    file = open(filename, 'w')

    file.write(str(size) + "\n")
    i = 1
    for city in data:
        file.write("{} {} {}\n".format(i, city[0], city[1]))
        i += 1
    
    file.close()

def Load(filename='./data/input.txt'):
    file = open(filename, 'r')

    size = int(file.readline())
    vertices = []

    for line in file:
        tmp = line.split()
        vertices.append([int(tmp[1]),int(tmp[2])])

    vertices = np.array(vertices)

    return vertices

def PathToFile(path):
    file = open("output.txt", 'w')

    for city in path:
        file.write(str(city)+"\n")

    file.close()

if __name__ == '__main__':

    opt = -1

    while opt != 0:
        print("\n\n0. Exit.")
        print("1. Generate random cities.")
        print("2. Load cities form file.")

        opt = input("Choose option: ")

        try:
            opt = int(opt)
        except:
            print("Please type a number!")
        else:
            if opt == 1:
                cities = Generate()
            elif opt == 2:
                cities = Load()
            elif opt == 0:
                exit()
            else:
                print("Wrong option!")
                continue
            break

    print(cities)
    
    opt = -1


    while opt != 0:
        print("\n\n0. Exit.")
        print("1. Greedy algorithm.")
        
        opt = input("Choose option: ")

        try:
            opt = int(opt)
        except:
            print("Please type a number!")
            continue
        else:
            if opt == 1:
                distance, result, coordinates = gd.main(cities)
            elif opt == 0:
                exit()
            else:
                print("Wrong option!")
                continue
            break

    print("Result:\n", result, "\nDistance:\n", distance)
    PathToFile(result)
    data = np.transpose(coordinates)
    pl.generateInteractiveGraph(x=data[0], y=data[1])