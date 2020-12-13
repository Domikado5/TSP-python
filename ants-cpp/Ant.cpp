#include "Ant.h"
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <stdlib.h>
#include <time.h>

using namespace std;

Ant::Ant(double alpha, double beta, vector<vector<int>>* cities, vector<vector<vector<double>>>* cities_matrix){
    this->alpha = alpha;
    this->beta = beta;
    this->cities = cities;
    this->cities_matrix = cities_matrix;
    this->check_unvisited();
}

void Ant::check_unvisited(){
    for(int i = 0; i < (*cities).size(); i++){
        this->unvisited_cities.push_back(i);
    }
}

int Ant::choose_city(){
    double total_unvisited_distance = 0.0;
    double attractiveness_sum = 0.0;
    int last_city = this->path.back();
    double random_attractiveness;
    double current_attractiveness = 0.0;

    for(auto &const unvisited_city: this->unvisited_cities){
        total_unvisited_distance += (*cities_matrix)[last_city][unvisited_city][0];
    }

    for(auto &const unvisited_city: this->unvisited_cities){
        attractiveness_sum += pow((*cities_matrix)[last_city][unvisited_city][1], this->alpha) * 
            (total_unvisited_distance / pow((*cities_matrix)[last_city][unvisited_city][0], this->beta));
    }

    uniform_real_distribution<double> unif(0.0, attractiveness_sum);
    default_random_engine re;
    random_attractiveness = unif(re);

    for(auto &const unvisited_city: this->unvisited_cities){
        current_attractiveness += pow((*cities_matrix)[last_city][unvisited_city][1], this->alpha) * 
            (total_unvisited_distance / pow((*cities_matrix)[last_city][unvisited_city][0], this->beta));
        
        if (current_attractiveness >= random_attractiveness){
            this->unvisited_cities.erase(remove(this->unvisited_cities.begin(), this->unvisited_cities.end(), unvisited_city), this->unvisited_cities.end());
            return unvisited_city;
        }
    }
}

void Ant::generate_path(){
    this->path.clear();
    this->distance = 0.0;
    srand(time(NULL));
    int random_city = rand() % (*cities).size();
    this->path.push_back(random_city);

    while(this->path.size() < (*cities).size()){
        random_city = this->choose_city();
        this->distance += (*cities_matrix)[this->path.back()][random_city][0];
        this->path.push_back(random_city);
    }
    
    this->distance += (*cities_matrix)[this->path.back()][this->path.front()][0];
    this->path.push_back(this->path.front());
}