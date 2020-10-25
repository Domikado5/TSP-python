import numpy as np
import random as rn
from numpy import version

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
    
    vertices = np.array(vertices)

    return vertices
        
def Load(filename='input.txt'):
    file = open(filename, 'r')

    size = int(file.readline())
    vertices = []

    for line in file:
        tmp = line.split(' ')
        vertices.append([int(tmp[1]),int(tmp[2])])

    vertices = np.array(vertices)

    return vertices


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
                result = 1 # your function here my boi
            elif opt == 0:
                exit()
            else:
                print("Wrong option!")
                continue
            break

    print(result)