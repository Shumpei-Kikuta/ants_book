#include <iostream>
using namespace std;
#define MAX 51

int n;
long int m;
long int K[MAX];

bool cal(){
    long int num;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            for (int k = 1; k <= n; k++){
                for (int l = 1; l <= n; l++){
                    num = K[i] + K[j] + K[k] + K[l];
                    if (num == m){
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main(){
    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        long int element;
        cin >> element;
        K[i]  = element;
    }
    if (cal()){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
    return 0;
}