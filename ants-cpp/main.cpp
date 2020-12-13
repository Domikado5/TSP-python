#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

double CalculateDistance(int x1, int y1, int x2, int y2){
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

vector<vector<int>> LoadData(string file_name){
    ifstream myfile(file_name.c_str());
    int size;
    int city, x, y;
    vector<vector<int>> data;
    vector<int> row;
    if(myfile.is_open()){
        myfile >> size;
        while(myfile >> city >> x >> y){
            row.push_back(city);
            row.push_back(x);
            row.push_back(y);
            data.push_back(row);
            row.clear();
        }
    }else{
        printf("File cannot be opened.\n");
    }
    return data;
}

vector<vector<vector<double>>> MakeMatrix(vector<vector<int>> data_input){
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

int main(){
    vector<vector<int>> cities; 
    vector<vector<vector<double>>> cities_matrix;

    cout << "START\n";

    cities = LoadData("./data/berlin52.txt");
    cities_matrix = MakeMatrix(cities);


    for(int i = 0; i < cities_matrix.size(); i++){
        for(int j = 0; j < cities_matrix[i].size(); j++){
            cout << cities_matrix[i][j][0] << " ";
        }
        cout << "\n";
    }

    return 0;
}