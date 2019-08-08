#include <iostream>
using namespace std;
#define MAX 100000
#include <vector>
#include <algorithm>

int n;
long int s[MAX], t[MAX];
vector<pair<long int, long int> > Time;

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> s[i] >> t[i];
        pair<long int, long int> time_;
        time_.first = t[i];
        time_.second = s[i];
        Time.push_back(time_);
    }
    sort(Time.begin(), Time.end());
    int ans = 0;
    int now = 0;
    for (int i = 0; i < n; i++){
        if (now <= Time[i].second){
            // 仕事の実行
            ans += 1;
            now = Time[i].first;
        }else{
            continue;
        }
    }
    cout << ans << endl;
    return 0;
}