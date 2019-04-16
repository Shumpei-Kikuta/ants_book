#include <iostream>
using namespace std;
#include <algorithm>
#define MAX_N 100000
#define INF 100000000

int n;
long int S;
int A[MAX_N];
int SUM[MAX_N];

void calc_sum(){
    SUM[0] = A[0];
    for (int i = 1; i <= n; i++){
        SUM[i] = SUM[i - 1] + A[i];
    }
}

int binary_search(int j, int left, int right){
    // summationがはじめてS以上となる点を探す
    if (left == right){
        return left;
    }else{
        int mid = (left + right) / 2;
        // cout << mid << endl;
        // cout << SUM[mid] << endl;
        cout << j << endl;
        if ((SUM[mid] - SUM[j])< S){
            return binary_search(j, mid + 1, right);
        }else{
            return binary_search(j, left, mid);
        }
    }
}

int main(){
    cin >> n >> S;
    A[0] = 0;
    for (int i = 1; i <= n; i++){
        cin >> A[i];
    }
    calc_sum();
    int ans = INF;
    for (int j = 1; j <= n; j++){
        if ((SUM[n] - SUM[j]) < S){
            continue;
        }
        int i = binary_search(j-1, j, n);
        // cout << j << endl;
        // cout << i - j + 1 << endl;
        ans = min(ans, i - j + 1);
    }
    cout << ans << endl;
    return 0;
}