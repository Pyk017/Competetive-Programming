#include<bits/stdc++.h>
using namespace std;

void display(int n, int mat[][4]){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << mat[i][j] << " ";
        }
        cout << "\n";
    }
}

void rotate(int n, int mat[][4]){
    for(int x = 0; x < n/2; x++){
        for(int y=x; y < n-x-1; y++){
            int temp = mat[x][y];
            mat[x][y] = mat[y][n - x - 1];
            mat[y][n - x - 1] = mat[n - x - 1][n - y - 1];
            mat[n - x - 1][n - y - 1] = mat[n - y - 1][x];
            mat[n - y - 1][x] = temp;
        }
    }
    display(n, mat);
}


int main(){

    int mat[4][4]{
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    rotate(4, mat);
    return 0;
}

