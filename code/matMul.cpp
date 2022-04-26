#include <stdlib.h>

int ** randomMatrix(int n){
    int** r;
    r = new int*[n];
    int i,j;
    for (i = 0; i < n; ++i) {
        for (j = 0;  j< n; ++j){
            r[i][j] = rand()%100;
        }
    }
    return r;
}

int ** matMul(int n ,int** m1,int** m2){
    int **r;
    r = new int*[n];
    int i,j,k;
    for (i = 0; i < n; ++i) {
        for (j = 0; j< n; ++j ) {
            int sum = 0;
            for (k = 0; k < n; ++k) {
                sum = sum + m1[i][k]* m2[k][j]; 
            }
            r[i][j] = sum;
        }
    }
    return r;
}
int main(void){
    int n = 1000;
    int ** r = randomMatrix(n);
    int ** h = matMul(n,r,r);
    return 0;
}
