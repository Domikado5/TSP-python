#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include "Colony.h"
#include "Ant.h"

using namespace std;

double CalculateDistance(int x1, int y1, int x2, int y2){
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

vector<vector<double>> LoadData(string file_name){
    ifstream myfile(file_name.c_str());
    int size;
    int city;
    double x, y;
    vector<vector<double>> data;
    vector<double> row;
    if(myfile.is_open()){
        myfile >> size;
        while(myfile >> city >> x >> y){
            row.push_back(city);
            row.push_back(x);
            row.push_back(y);
            data.push_back(row);
            row.clear();
        }
        myfile.close();
    }else{
        printf("File cannot be opened.\n");
    }
    return data;
}

vector<vector<vector<double>>> MakeMatrix(vector<vector<double>> data_input){
    vector<vector<vector<double>>> data_output;
    vector<vector<double>> data_row;
    vector<double> data_cell;
    double distance;
    for(int i = 0; i < data_input.size(); i++){
        for(int j = 0; j < data_input.size(); j++){
            if(i == j){
                data_cell.push_back(0.0); // distance / weight
                data_cell.push_back(0.0); // pheromones
            }else{
                distance = CalculateDistance(data_input[i][1], data_input[i][2], data_input[j][1], data_input[j][2]);
                data_cell.push_back(distance); // distance / weight
                data_cell.push_back(1.0); // pheromones
            }
            data_row.push_back(data_cell);
            data_cell.clear();
        }
        data_output.push_back(data_row);
        data_row.clear();
    }

    return data_output;
}
// program filename ant_count steps alpha beta rho

int main(int argc, char* argv[]){
    if(argc < 7){
        cout << "Missing arguments\n";
        return 0;
    }
    vector<vector<double>> cities; 
    vector<vector<vector<double>>> cities_matrix;
    double min_scalling_factor = 0.001;
    double pheromone_weight = 1.0;

    cities = LoadData(argv[1]);
    cities_matrix = MakeMatrix(cities);

    Colony aco = Colony(atoi(argv[2]), min_scalling_factor,
        atof(argv[4]), atof(argv[5]), atof(argv[6]), atoi(argv[3]),
        &cities, &cities_matrix, pheromone_weight);
    
    cout << "Started solving\n";
    aco.solve();
    vector<int> path = aco.get_path();
    double distance = aco.get_distance();

    ofstream myFile("./output.txt");
    myFile << distance << "\n";
    myFile << path.size() << "\n";
    for(int i = 0; i < path.size(); i++){
        myFile << cities[path[i]][0] << " " << cities[path[i]][1] << " " << cities[path[i]][2] << "\n";
    }
    myFile.close();
    cout << "Finished solving\n";
    // cout << "Sciezka: \n";
    // for(int i = 0; i < path.size(); i++){
    //     cout << path[i] << " ";
    // } cout << "\n";
    // cout << "Dystans: " << distance << "\n";

    return 0;
}