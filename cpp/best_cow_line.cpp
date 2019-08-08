#include <iostream>
#include <vector>
using namespace std;

vector<char> S;
vector<char> T;

int N;

void search_minimum(int top, int bottom, int n){
    if (top == bottom){
        T.push_back(S[top]);
        for (int i = 0; i < N; i++){
            cout << T[i];
        }
        cout << endl;
    }
    else{
        if (S[top] < S[bottom]){
            // bottom側の方が大きい時→例えば，先頭がA, 後ろがV
            T.push_back(S[top]);
            top += 1;
        }else if(S[top] > S[bottom]){
            T.push_back(S[bottom]);
            bottom -= 1;
        }else if(S[top] == S[bottom]){
            int num = 1;
            while(true){
                if (top + num == bottom - num){
                    // 残りが同じ文字
                    T.push_back(S[top]);
                    top += 1;
                    break;
                }
                else{
                    if (S[top + num] < S[bottom - num]){
                        T.push_back(S[top]);
                        top += 1;
                        break;
                    }else if (S[top + num] > S[bottom - num]){
                        T.push_back(S[bottom]);
                        bottom -= 1;
                        break;
                    }
                    num += 1;
                }
            }
        }
        n += 1;
        cout << top << " " << bottom << " " << n << endl;
        search_minimum(top, bottom, n);
    }
}

int main(){
    cin >> N;
    for (int i = 0; i < N; i++){
        char element;
        cin >> element;
        S.push_back(element);
    }
    // for (int i = 0; i < N; i++){
    //     cout << S[i] << endl;
    // }
    int top = 0;
    int bottom = N - 1;
    search_minimum(top, bottom, 0);
    return 0;
}