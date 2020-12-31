#ifndef ANT_H   
#define ANT_H
#include <vector>

using namespace std;

class Ant
{
    private:
        double distance = 0.0;
        vector<int> path;
        double alpha;
        double beta;
        vector<vector<double>>* cities;
        vector<vector<vector<double>>>* cities_matrix;
        vector<int> unvisited_cities;
    public:
        Ant(double alpha, double beta, vector<vector<double>>* cities, vector<vector<vector<double>>>* cities_matrix);
        int choose_city();
        void generate_path();
        void check_unvisited(); // return list of unvisited cities
        vector<int> show_path();
        double show_distance();
};

#endif