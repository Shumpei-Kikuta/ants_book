#include <iostream>
#include <stdio.h>
using namespace std;
#define MAX_N 10000
#include <cmath>
#include <iomanip>

int N, K;
double L[MAX_N];

double binary_search(double left, double right){
    for (int j = 0; j < 100; j++){
        double mid = (left + right) / 2;
        int c = 0;
        for (int i = 0; i < N; i++){
            c += floor(L[i] / mid);
        }
        if (c >= K){
            left = mid;
        }
        else{
            right = mid;
        }
    }
    return left;
}

int main(){
    // initialize
    cin >> N >> K;
    for (int i = 0; i < N; i++){
        cin >> L[i];
    }
    printf("%.1f\n", binary_search(0.0, 10000.0));
    return 0;
}