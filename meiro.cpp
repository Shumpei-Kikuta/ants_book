#include <iostream>
using namespace std;
#define wall -2
#include <queue>
#include <tuple>

struct tup{
    int x;
    int y;
    int num;
};

int H, W;
int sx, sy;
int gx, gy;
int matrix[52][52];
queue <tup> Q;
int main(){
    cin >> H >> W >> sx >> sy >> gx >> gy;
    for (int i = 0; i <= H + 1; i++){
        for (int j = 0; j <= W + 1; j++){
            matrix[i][j] = -2;
        }
    }
    for (int i = 1; i <= H; i++){
        for (int j = 1; j <= W; j++){
            char element;
            cin >> element;
            if (element == '#'){
                matrix[i][j] = wall;
            }else{
                matrix[i][j] = -1;
            }
        }
    }
    tup now;
    now.x = sx;
    now.y = sy;
    now.num = 0;
    Q.push(now);
    while ((!Q.empty())){
        now = Q.front();
        matrix[now.x][now.y] = now.num;
        if (( now.x== gx) && (now.y == gy)){
            cout << now.num << endl;
            break;
        }
        for (int i = -1; i <= 1; i++){
            for (int j = -1; j <= 1; j++){
                if ((i + j) % 2 == 0){
                    continue;
                }
                if (matrix[now.x + i][now.y + j] == -1){
                    tup next;
                    next.x = now.x + i;
                    next.y = now.y + j;
                    next.num = now.num + 1;
                    Q.push(next);
                }
            }
        }
        Q.pop();
    }
    // for (int i = 0; i <= H + 1; i++){
    //     for (int j = 0; j <= W + 1; j++){
    //         cout << matrix[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    return 0;
}