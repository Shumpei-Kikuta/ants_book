#include <iostream>
using namespace std;
#define MAX 52


void depth_search(int w, int h, int is_lands[MAX][MAX], int i, int j){
    if (is_lands[i][j] == 1){
        is_lands[i][j] = 0;
        for (int k = -1; k <= 1; k++){
            for (int m = -1; m <= 1; m++){
                depth_search(w, h, is_lands, i, j);
            }
        }
    }
}

int main(){
    while (true){
        int w, h;
        int is_lands[MAX][MAX]={};
        cin >> w >> h;
        for (int i = 1; i <= h; i++){
            for (int j = 1; j <= w; j++){
                int element;
                cin >> element;
                is_lands[i][j] = element;
            }
        }
        int num = 0;
        for (int i = 1; i <= h; i++){
            for (int j = 1; j <= w; j++){
                if (is_lands[i][j] == 0){
                    continue;
                }else{
                    // 島の発見
                    depth_search(w, h, is_lands, i, j);
                    num += 1;
                }
            }
        }
        cout << num << endl;
    }
    return 0;
}