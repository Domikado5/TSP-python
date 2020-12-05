from greedy import calc_dist
import numpy as np
import random as rn

def distance_matrix(cities):
    matrix = []
    for city in cities:
        row = []
        for city2 in cities:
            row.append(calc_dist(city[0], city[1], city2[0], city2[1]))
        matrix.append(row)
    return np.array(matrix)

class Colony:
    def __init__(self, ant_count, min_scalling_factor=0.001, alpha=1.0, beta=3.0, rho=0.1, steps=100, cities=[], pheromone_weight=1.0):
        self.ant_count = ant_count # colony size
        self.ants = [Ant(self) for _ in range(self.ant_count)]

        self.min_scalling_factor = min_scalling_factor
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.steps = steps

        self.cities = cities
        self.cities_count = len(cities)
        self.distance_matrix = distance_matrix(cities)

        self.pheromones = np.full([self.cities_count, self.cities_count], 1.0)
        self.pheromone_weight = pheromone_weight
        
        self.path_result = []
        self.distance_result = np.inf

    def place_pheromone(self, path, distance):
        pheromone_amount = self.pheromone_weight / distance
        for i in range(self.cities_count):
            self.pheromones[path[i]][path[(i + 1) % self.cities_count]] = pheromone_amount

    def solve(self): # solve using max min algorithm
        for step in range(self.steps):
            best_path = []
            best_distance = np.inf
            for ant in self.ants:
                ant.generate_path()
                if ant.total_distance < best_distance:
                    best_distance = ant.total_distance
                    best_path = ant.path
            if best_distance < self.distance_result:
                self.distance_result = best_distance
                self.path_result = best_path
            self.place_pheromone(self.path_result, self.distance_result)
            max_pheromone = self.pheromone_weight / self.distance_result
            min_pheromone = max_pheromone * self.min_scalling_factor
            # dalej robimy numpy mnozenier macierzy etc.


class Ant:
    def __init__(self, Colony : Colony):
        self.Colony = Colony
        self.total_distance = 0.0
        self.path = []

    def choose_city(self):
        unvisited_cities = np.setxor1d(self.path, self.Colony.cities)
        total_unvisited_distance = 0.0
        attractiveness_sum = 0.0
        for unvisited_city in unvisited_cities:
            total_unvisited_distance += self.Colony.distance_matrix[self.path[-1]][unvisited_city]
            attractiveness_sum += self.Colony.pheromones[self.path[-1]][unvisited_city]**self.Colony.alpha *\
                (total_unvisited_distance / self.Colony.distance_matrix[self.path[-1]][unvisited_city])**self.Colony.beta
        random_attractiveness = rn.uniform(0.0, attractiveness_sum) # randomizing the attractiveness, which normally would be a probability of choosing a city
        current_attractievness = 0.0
        for unvisited_city in unvisited_cities: # searching for the city which have the choosen attractiveness
            current_attractievness += self.Colony.pheromones[self.path[-1]][unvisited_city]**self.Colony.alpha *\
                (total_unvisited_distance / self.Colony.distance_matrix[self.path[-1]][unvisited_city])**self.Colony.beta
            if current_attractievness >= random_attractiveness:
                return unvisited_city

    def generate_path(self):
        self.path.append(rn.randint(0, self.Colony.cities_count -1))
        while self.Colony.cities_count > len(self.path):
            self.path.append(self.choose_city())
            self.total_distance += self.Colony.distance_matrix[self.path[-2]][self.path[-1]]