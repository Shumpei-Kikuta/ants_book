#include <iostream>
using namespace std;

int payment, change;
int coins[6] = {500, 100, 50, 10, 5, 1};
int main(){
    cin >> payment;
    change = 1000 - payment;
    int num = 0;
    for (int i = 0; i < 6; i++){
        while(true){
            if (change >= coins[i]){
                change -= coins[i];
                num += 1;
            }
            else{
                break;
            }
        }
    }
    cout << num << endl;
    return 0;
}