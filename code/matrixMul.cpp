
#include "matrixMul.h"
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <ctime>
#include <random>

using namespace std;



matrixMul::matrixMul(int dim) {
dimension=dim;
populate();
}

void matrixMul::populate() {
    for (int x=0;x<dimension;x++){
        for (int y=0;y<dimension;y++){
            std::default_random_engine generator;
            std::uniform_int_distribution<int> distribution(3,5);
            int x = distribution(generator);
            afil.push_back(x);

        }
        result.push_back(afil);
        a.push_back(afil);
    }
    for (int x=0;x<dimension;x++){
        for (int y=0;y<dimension;y++){
            std::default_random_engine generator;
            std::uniform_int_distribution<int> distribution(0,5);
            int x = distribution(generator);
            bfil.push_back(x);

        }
        b.push_back(afil);
    }
}

void matrixMul::see() {
    for (int x=0;x<dimension;x++){
        for (int y=0;y<dimension;y++){
          cout<<a[x][y]<<" ";
        }
        cout<<endl;
    }
    for (int x=0;x<dimension;x++){
        for (int y=0;y<dimension;y++){
            cout<<b[x][y]<<" ";
        }
        cout<<endl;
    }
}

void matrixMul::getResult() {
    for (int x=0;x<dimension;x++){
        for (int y=0;y<dimension;y++){
            cout<<result[x][y]<<" ";
        }
        cout<<endl;
    }
}

void matrixMul::multiply() {
    for (int z = 0; z < dimension; z++) {
        for (int x = 0; x < dimension; x++) {
            int res = 0;
            for (int y = 0; y < dimension; y++) {
                res +=a[x][y] * b[y][z];
            }
            result[x][z]=res;
        }
    }

}
