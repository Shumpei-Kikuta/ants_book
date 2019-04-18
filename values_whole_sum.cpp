#include <iostream>
using namespace std;
#define MAX_N 5000
#include <vector>
#include <algorithm>

int n;
long int A[MAX_N], B[MAX_N], C[MAX_N], D[MAX_N];
vector<long int> AB;

void initialize(long int *K){
    for (int i = 0; i < n; i++){
        cin >> K[i];
    }
}

bool binary_search(int left, int right, long int value){
    long int mid = (left + right) / 2;
    if (value == AB[mid]){
        return true;
    }else if (left == right){
        return false;
    }else if(value > AB[mid]){
        return binary_search(mid + 1, right, value);
    }else{
        return binary_search(left, mid, value);
    }
}

int main(){
    cin >> n;
    initialize(A);initialize(B);initialize(C);initialize(D);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            AB.push_back(A[i] + B[j]);
        }
    }
    sort(AB.begin(), AB.end());
    int num = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (binary_search(0, AB.size() - 1, - (C[i] + D[j]))){
                num += 1;
            }
        }
    }
    cout << num << endl;
    return 0;
}