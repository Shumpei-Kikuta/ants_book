#include <iostream>
using namespace std;
#define MAX 10001

long int N;
bool is_primes[MAX];
long int num;

int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        is_primes[i] = true;
    }
    for (int i = 2; i < N; i++){
        if (!is_primes[i]){
    //         // 素数でないとわかっている場合
            continue;
        }else{
    //         // 素数の時
            num += 1;
            for (int j = i + 1; j < N; j++){
                if ((j % i) == 0){
                    is_primes[j] = false;
                }
            }
        }
    }
    cout << num << endl;
    return 0;
}