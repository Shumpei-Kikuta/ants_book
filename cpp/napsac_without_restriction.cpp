#include <iostream>
using namespace std;
#define MAX_N 101
#define MAX_W 10001
#include <algorithm>

int N;
int w[MAX_N], v[MAX_N];
int W;
int dp[MAX_W][MAX_W] ={0};
int main(){
    cin >> N >> W;
    for (int i = 1; i <= N; i++){
        int wi, vi;
        cin >> vi >> wi;
        w[i] = wi;
        v[i] = vi;
    }
    // O(NW^2)
    // for (int i = 0; i <= W; i++){
    //     for (int j = 0; j <= W; j++){
    //         for (int k = 0; k < n; k++){
    //             if (j + w[k] <= W){
    //                 dp[i + 1][j + w[k]] = max(dp[i][j] + v[k], dp[i + 1][j + w[k]]);
    //             }
    //         }
    //     }
    // }
    // cout << dp[W][W] << endl;

    // O(NW)
    for (int i = 1; i <= N; i++){
        for (int j = 0; j <= W; j++){
            if (j < w[i]){
                dp[i][j] = dp[i - 1][j];
            }else{
                dp[i][j] = max(dp[i-1][j], dp[i][j - w[i]] + v[i]);
            }
            // cout << dp[i][j] << " ";
        }
        // cout << endl;
    }
    cout << dp[N][W] << endl;

    return 0;
}