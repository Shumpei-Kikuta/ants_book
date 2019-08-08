#include <iostream>
using namespace std;
#define MAX_N 100
#define MAX_W 10000
#include <vector>
#include <algorithm>

int n;
int W;
pair<int, int> good;
pair<int, int> goods[MAX_N];
int dp[MAX_N][MAX_W];

int depth_first_search(int num, int rest_weight){
    int res;
    if (num == n){
        res = 0;
    }
    if(dp[num][rest_weight] != -1){
        res = dp[num][rest_weight];
    }
    else if(rest_weight < goods[num].first){
         dp[num+1][rest_weight] = depth_first_search(num+1, rest_weight);
         res = dp[num+1][rest_weight];
    }
    else{
        dp[num+1][rest_weight] = max(depth_first_search(num+1, rest_weight - goods[num].first) + goods[num].second, depth_first_search(num+1, rest_weight));
        return dp[num+1][rest_weight];
    }
    return res;
}

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> good.first >> good.second;
        goods[i] = good;
    }
    cin >> W;
    for (int i = 0; i < n; i++){
        for (int j = 0; j <= W; j++){
            dp[i][j] = -1;
        }
    }
    cout << depth_first_search(0, W) << endl;
    for (int i = 0; i < n; i++){
        for (int j = 0; j <= W; j++){
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}