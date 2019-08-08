#include <iostream>
using namespace std;
#define MAX 1000001

int n;
long int k;
long int lists[MAX];

int binary_search(int left, int right){
    if (left == right){
        return left;
    }
    else{
        int mid = (left + right) / 2;
        if (lists[mid] >= k){
            return binary_search(left, mid);
        }else{
            return binary_search(mid + 1, right);
        }
    }
}

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        long int element;
        cin >> element;
        lists[i] = element;
    }
    cin >> k;
    cout << binary_search(0, n - 1) << endl;
    return 0;
}