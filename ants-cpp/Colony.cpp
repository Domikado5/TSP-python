#include "Colony.h"
#include <vector>

using namespace std;

Colony::Colony(int ant_count, double min_s_f, double alpha,
            double beta, double rho, int steps,
            vector<vector<int>>* cities, vector<vector<vector<double>>>* cities_matrix,
            double pheromone_weight)
{
    this->ant_count = ant_count;

    for(int i = 0; i < ant_count; i++){
        this->ants.push_back(Ant(alpha, beta, cities, cities_matrix));
    }

    this->min_scalling_factor = min_s_f;
    this->rho = rho;
    this->steps = steps;
    this->cities = cities;
    this->cities_matrix = cities_matrix;
    this->pheromone_weight = pheromone_weight;
}

void Colony::solve(){
    
}

void Colony::place_pheromones(vector<int> path, double distance){
    double pheromone_amount = this->pheromone_weight / distance;
    for(int i = 0; i < path.size() - 1; i++){
        (*this->cities_matrix)[path[i]][path[i+1]][1] = (*this->cities_matrix)[path[i+1]][path[i]][1] += pheromone_amount;
    }
}