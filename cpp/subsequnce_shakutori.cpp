#include <iostream>
using namespace std;
#include <algorithm>

int n, S;
int A[10000];
int SUM[10000];

void calc_sum(){
    // i 番目までの和
    SUM[0] = A[0];
    for (int i = 0; i < n; i++){
        SUM[i] = SUM[i - 1] + A[i];
    }
}

int main(){
    cin >> n >> S;
    for (int i = 0; i < n; i++){
        cin >> A[i];
    }
    calc_sum();
    int ans = 100000;
    int j = 0;
    int i = 0;
    while ((i < n) && (j < n)) {
        if (SUM[j] - SUM[i] < S){
            j++;
        }else{
            ans = min(ans, j - i);
            i++;
        }
    }
    cout << ans << endl;
    return 0;
}