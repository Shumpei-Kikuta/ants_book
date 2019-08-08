#include <iostream>
using namespace std;
#include <cmath>

long int N;

bool is_factorial(){
    long int until = pow(N, 0.5);
    for (int i = 2; i <= until; i++){
        if (N % i == 0){
            return true;
        }
    }
    return false;
}

int main(){
    cin >> N;
    if (is_factorial()){
        cout << "NO" << endl;
    }else{
        cout << "YES" << endl;
    }
    return 0;
}