#include <iostream>
using namespace std;
#define MAX_A 100001
#define MAX_M 100001
#define MAX_N 101
#define MAX_K 100000

int n;
int A[MAX_A];
int M[MAX_M];
int K;
int dp[MAX_N][MAX_K];

int main(){
    cin >> n;
    for (int i = 1; i <= n; i++){
        int ai;
        cin >> ai;
        A[i] = ai;
    }
    for (int i = 1; i <= n; i++){
        int mi;
        cin >> mi;
        M[i] = mi;
    }
    cin >> K;
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= K; j++){
            dp[i][j] = -1;
        }
    }
    dp[0][0] = 0;

    for (int i = 1; i <= n; i++){
        for (int j = 0; j <= K; j++){
            if (dp[i - 1][j] >= 0){
                dp[i][j] = M[i];
            }
            else if (dp[i][j - A[i]] >= 0){
                dp[i][j] = dp[i][j - A[i]] - 1;
            }
            else{
                dp[i][j] = -1;
            }
        }
    }
    if (dp[n][K] >= 0){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }

    return 0;
}