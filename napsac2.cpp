#include <iostream>
using namespace std;
#define MAX 101
#include <algorithm>

int n;
pair<long int, int> goods[MAX];
long int W;
long int dp[MAX][MAX*MAX] = {0};

int main(){
    cin >> n;
    for (int i = 0; i < n ;i++){
        long int w;
        int v;
        cin >> w >> v;
        goods[i] = make_pair(w, v);
    }
    cin >> W;
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= n * MAX; j++){
            if ((j == 0) || (i == 0)){
                continue;
            }
            else{
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - goods[i].second] + goods[i].first);
            }
        }
    }
    // 修正が必要
    return 0;
}