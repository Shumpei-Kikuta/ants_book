#include <iostream>
using namespace std;
#include <queue>
#include <algorithm>

priority_queue<int> L;
int N;

int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        int element;
        cin >> element;
        L.push(-element);
    }
    int cost = 0;
    while(L.size() > 1){
        int new_line = L.top();
        L.pop();
        new_line += L.top();
        L.pop();
        cost += new_line;
        L.push(new_line);
    }
    cout << -cost << endl;
    return 0;
}