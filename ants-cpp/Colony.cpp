#include "Colony.h"
#include <vector>
#include <iostream>
#include <limits>

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
    this->distance_result = numeric_limits<double>::max();
}

void Colony::solve(){
    vector<int> best_path;
    double best_distance, max_pheromone, min_pheromone;
    for (int step = 0; step < steps; step++){
        best_path.clear();
        best_distance = numeric_limits<double>::max();
        for (int ant = 0; ant < this->ant_count; ant++){
            (this->ants)[ant].generate_path();
            if ((this->ants)[ant].show_distance() < best_distance){
                best_distance = (this->ants)[ant].show_distance();
                best_path = (this->ants)[ant].show_path();
            }
        }
        if (best_distance < this->distance_result){
            this->distance_result = best_distance;
            this->path_result = best_path;
        }
        this->place_pheromones(this->path_result, this->distance_result);
        max_pheromone = this->pheromone_weight / this->distance_result;
        min_pheromone = max_pheromone * this->min_scalling_factor;
        for(int i = 0; i < (*this->cities_matrix).size(); i++){
            for(int j = 0; j < i; j++){
                (*this->cities_matrix)[i][j][1] *= (1.0 - this->rho);
                (*this->cities_matrix)[j][i][1] = (*this->cities_matrix)[i][j][1];
                if((*this->cities_matrix)[i][j][1] > max_pheromone){
                    (*this->cities_matrix)[i][j][1] = (*this->cities_matrix)[j][i][1] = max_pheromone;
                }else if((*this->cities_matrix)[i][j][1] < min_pheromone){
                    (*this->cities_matrix)[i][j][1] = (*this->cities_matrix)[j][i][1] = min_pheromone;
                }
            }
        }
    }
}

void Colony::place_pheromones(vector<int> path, double distance){
    double pheromone_amount = this->pheromone_weight / distance;
    for(int i = 0; i < path.size() - 1; i++){
        (*this->cities_matrix)[path[i]][path[i+1]][1] = (*this->cities_matrix)[path[i+1]][path[i]][1] += pheromone_amount;
    }
}

double Colony::get_distance(){
    return this->distance_result;
}

vector<int> Colony::get_path(){
    return this->path_result;
}