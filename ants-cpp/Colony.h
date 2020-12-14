#ifndef COLONY_H
#define COLONY_H
#include <vector>
#include "Ant.h"

using namespace std;

class Colony
{
    private:
        int ant_count;
        vector<Ant> ants;
        double rho;
        vector<vector<int>>* cities;
        vector<vector<vector<double>>>* cities_matrix;
        int steps;
        double min_scalling_factor;
        double pheromone_weight;
        double distance_result = 0.0;
        vector<int> path_result;
    public:
        Colony(int ant_count, double min_s_f, double alpha,
            double beta, double rho, int steps,
            vector<vector<int>>* cities, vector<vector<vector<double>>>* cities_matrix,
            double pheromone_weight);
        void solve();
        void place_pheromones(vector<int> path, double distance);
        double get_distance();
        vector<int> get_path();
};

#endif