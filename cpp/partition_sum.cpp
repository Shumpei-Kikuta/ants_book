#include <iostream>
using namespace std;
#define MAX 20

int n;
long int A[MAX];
long int k;
long int num;
bool flag=false;

void recursive(long int num, int place){
    if ((place < n) && (num < k)){
        recursive(num + A[place], place + 1);
        recursive(num, place+1);
    }
    else{
        if (num == k){
            flag = true;
        }
    }
}

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        long int element;
        cin >> element;
        A[i] = element;
    }
    cin >> k;
    recursive(0, 0);
    if (flag){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
    

    return 0;
}