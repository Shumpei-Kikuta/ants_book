#include <iostream>
using namespace std;
#define MAX_n 1000
#define MAX_M 10000

int n, m, M;
int dp[MAX_M+1][MAX_n+1] = {};
int main(){
    cin >> n >> m >> M;
    for (int i = 1; i <= n;ni++){
        for (int j = 0; j <= m; j++){
            if (j == 0){
                dp[j][1] = 1;
                continue;
            }
            if (j - i >= 0){
                dp[j][i] = (dp[j - i][i] + dp[j][i - 1]) % M;
            }else{
                dp[j][i] = (dp[j][i - 1]) % M;
            }
        }
    }
    cout << dp[n][m] << endl;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            cout << dp[j][i] << " ";
        }
        cout << endl;
    }

    return 0;
}