#include <iostream>
using namespace std;
#include <queue>
#include <vector>

int N, L, P;
vector<pair<int, int> > Stations;
priority_queue<int> Q;


int calculate_oil_num(){
    int num = 0;
    int oil = P;
    for (int i = 1; i <= N + 1; i++){
        Q.push(Stations[i].second);
        oil -= Stations[i].first - Stations[i - 1].first;
        // oilの給油が必要か
        while(true){
            if (Q.empty()){
                return -1;
            }
            else if (oil >= 0){
                break;
            }
            else{
                num += 1;
                oil += Q.top();
                Q.pop();
            }
        }
    }
    return num;
}

int main(){
    cin >> N >> L >> P;
    Stations.push_back(make_pair(0, 0));
    for (int i = 0; i < N; i++){
        int a, b;
        cin >> a >> b;
        Stations.push_back(make_pair(a, b));
    }
    Stations.push_back(make_pair(L, 0));
    cout << calculate_oil_num() << endl;
    return 0;
}