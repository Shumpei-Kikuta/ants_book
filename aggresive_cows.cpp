#include <iostream>
using namespace std;
#define MAX_N 100000
#define MAX_d 1000000000

int N, M;
long int X[MAX_N];

// long int binary_search(long int d){
//     // Lの中でmidより大きい最も小さい値を返す
//     int left = 0;
//     int right = N - 1;
//     while(left != right){
//         int mid = (left + right) / 2;
//         if (X[mid] )
//     }
// }

bool is_short(long int right, long int mid){
    int last_node = 0;
    long int now = 0;
    int m = 0;
    for (int i = 1; i < N; i++){
        if (X[i] - X[last_node] < mid){
            continue;
        }else{
            m += 1;
            last_node = i;
        }
        if (now > X[N - 1]){
            return false;
        }
        if (m >= M){
            return true;
        }
    }
}

int main(){
    // initialize
    cin >> N >> M;
    for (int i = 0; i < N; i++){
        cin >> X[i];
    }

    // maximize
    long int left = X[0];
    long int right = X[N - 1];
    for (int i = 0; i < 100; i++){
        long int mid = (right + left) / 2;
        if (is_short(right, mid)){
            left = mid;
        }else{
            right = mid;
        }
    }
    cout << left << endl;
    return 0;
}