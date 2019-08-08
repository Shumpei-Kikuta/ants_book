#include <iostream>
using namespace std;
#define MAX 1001
#include <string>
#include <algorithm>

int num;
int n, m;
string s, t;
int dp[MAX][MAX] = {0};

int main(){
    cin >> num;
    for (int k = 0; k < num; k++){
        cin >> s;
        cin >> t;
        n = s.length();
        m = t.length();
        for (int i = 0; i < s.length(); i++){
            for (int j = 0; j < t.length(); j++){
                if (s[i] == t[j]){
                    dp[i + 1][j + 1] = max(dp[i][j] + 1, max(dp[i + 1][j], dp[i][j + 1]));
                }
                else{
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        cout << dp[n][m] << endl;
    }
    return 0;
}