from main import Generate, Load
import greedy
import aco

files = ['bier127.txt']
for file in files:
    print(file)
    # cities = Load(filename='./data/' + file)
    cities = Generate(size=10)
    distance, path, coord = greedy.main(cities)
    print('Greedy: {}'.format(distance))
    jar_of_ants = aco.Colony(ant_count=10, cities=cities, steps=100)
    jar_of_ants.solve()
    print('ACO: {}\n'.format(jar_of_ants.distance_result))