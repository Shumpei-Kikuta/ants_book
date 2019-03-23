#include <iostream>
using namespace std;
#define MAX 100
#include <vector>
#include <algorithm>

int n;
int W;
pair<int, int> good;
pair<int, int> goods[MAX];
vector<int> lists;

int depth_first_search(int num, int rest_weight){
    int res;
    if (num == n){
        res = 0;
    }
    else if(rest_weight < goods[num].first){
        res = depth_first_search(num+1, rest_weight);
    }
    else{
        res = max(depth_first_search(num+1, rest_weight - goods[num].first) + goods[num].second, depth_first_search(num+1, rest_weight));
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
    cout << depth_first_search(0, W) << endl;
    return 0;
}