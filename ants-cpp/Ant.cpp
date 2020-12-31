#include "Ant.h"
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <ctime>
#include <stdlib.h>
#include <time.h>
#include <iostream>

using namespace std;


Ant::Ant(double alpha, double beta, vector<vector<double>>* cities, vector<vector<vector<double>>>* cities_matrix){
    this->alpha = alpha;
    this->beta = beta;
    this->cities = cities;
    this->cities_matrix = cities_matrix;
    this->check_unvisited();
}

void Ant::check_unvisited(){
    this->unvisited_cities.clear();
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
    int index;

    for(auto const& unvisited_city: this->unvisited_cities){
        total_unvisited_distance += (*cities_matrix)[last_city][unvisited_city][0];
    }

    for(auto const& unvisited_city: this->unvisited_cities){
        attractiveness_sum += pow((*cities_matrix)[last_city][unvisited_city][1], this->alpha) * 
            (total_unvisited_distance / pow((*cities_matrix)[last_city][unvisited_city][0], this->beta));
    }
    
    default_random_engine re(time(0));
    uniform_real_distribution<double> unif(0.0, attractiveness_sum);
    random_attractiveness = unif(re);

    for(auto const& unvisited_city: this->unvisited_cities){
        current_attractiveness += pow((*cities_matrix)[last_city][unvisited_city][1], this->alpha) * 
            (total_unvisited_distance / pow((*cities_matrix)[last_city][unvisited_city][0], this->beta));
        
        if (current_attractiveness >= random_attractiveness){
            return unvisited_city;
        }
    }
}

void Ant::generate_path(){
    this->path.clear();
    this->check_unvisited();
    this->distance = 0.0;
    default_random_engine re(time(0));
    uniform_int_distribution<int> distribution(0, (*cities).size()-1);
    int random_city = distribution(re);
    this->path.push_back(random_city);
    this->unvisited_cities.erase(remove(this->unvisited_cities.begin(), this->unvisited_cities.end(), random_city), this->unvisited_cities.end());

    while(this->path.size() < (*this->cities).size()){
        random_city = this->choose_city();
        this->distance += (*cities_matrix)[this->path.back()][random_city][0];
        this->path.push_back(random_city);
        this->unvisited_cities.erase(remove(this->unvisited_cities.begin(), this->unvisited_cities.end(), random_city), this->unvisited_cities.end());
    }
    
    this->distance += (*cities_matrix)[this->path.back()][this->path.front()][0];
    this->path.push_back(this->path.front());
}

vector<int> Ant::show_path(){
    return this->path;
}

double Ant::show_distance(){
    return this->distance;
}