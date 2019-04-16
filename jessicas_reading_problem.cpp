#include <iostream>
using namespace std;
#include <algorithm>
#include <map>
#define MAX_P 1000000

int P;
int A[MAX_P];
bool uA[MAX_P];
map<int, int> project_dicts;

bool is_complete(int *Ans, int num){
    int cnum = 0;
    for (long int i = 0; i < MAX_P; i++){
        if (Ans[i] >= 0){
            cnum += 1;
        }
    }
    // cout << cnum << endl;
    if (cnum == num){
        return true;
    }else{
        return false;
    }
}

int main(){
    cin >> P;
    for (long int i = 0; i < MAX_P; i++){
        uA[i] = false;
    }
    for (int i = 0; i < P; i++){
        cin >> A[i];
        uA[A[i]] = true;
    }
    int num = 0;
    for (long int i = 0; i < MAX_P; i++){
        if (uA[i]){
            // project_dicts[i] = num;
            num += 1;
        }
    }
    // for (int i = 0;i < P; i++){
    //     A[i] = project_dicts[A[i]];
    // }
    int ans = P;
    int i = 0;
    int j = 0;
    int Ans[MAX_P];
    for (long int  i = 0; i < MAX_P; i++){
        Ans[i] = -1;
    }
    // cout << num << endl;
    while((i < P) && (j < P)){
        if (is_complete(Ans, num)){
            Ans[A[i]] -= 1;
            ans = min(ans, j - i);
            i++;
        }else{
            Ans[A[j]] += 1;
            // cout << A[j] << endl;
            // cout << Ans[1] << endl;
            j++;
        }
        // cout << i << " " << j << endl;
    }
    cout << ans << endl;
    return 0;
}