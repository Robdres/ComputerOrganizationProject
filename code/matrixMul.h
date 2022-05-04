//
// Created by sjuan on 5/2/2022.
//

#ifndef CPPMATRIX_MATRIXMUL_H
#define CPPMATRIX_MATRIXMUL_H
#include <vector>

using namespace std;


class matrixMul {
    void populate();




public:
    matrixMul(int dime);
    void multiply();
    void see();
    void getResult();

private:
    int dimension;
    vector<vector<int>> result;
    vector<vector<int>> a;
    vector<vector<int>> b;
    vector<int> rfil;
    vector<int> afil;
    vector<int> bfil;




};


#endif //CPPMATRIX_MATRIXMUL_H
