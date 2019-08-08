#include <iostream>
using namespace std;
#define MAX_N 1000001

int n;
int A[MAX_N];
pair<int, int> dp[MAX_N];
int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        int ai;
        cin >> ai;
        A[i] = ai;
    }
    // initialize
    dp[0].first = 0;
    dp[0].second = -1;
    for (int i = 1; i < n; i++){
        if (A[i] > dp[i - 1].second){
            dp[i] = make_pair(dp[i - 1].first + 1, A[i]);
        }else{
            dp[i] = make_pair(dp[i - 1].first, dp[i - 1].second);
        }
    }
    cout << dp[n - 1].first << endl;
    return 0;
}