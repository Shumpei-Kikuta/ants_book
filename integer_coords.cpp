#include <iostream>
using namespace std;
#include <algorithm>

long int x1, x2, y1, y2;

long int euclidean_algorithm(long int x, long int y){
    if ((x == 0 ) || (y == 0)){
        return max(x, y);
    }else{
        return euclidean_algorithm(max(x, y) % (min(x, y)), min(x, y));
    }
}

int main(){
    cin >> x1 >> y1 >> x2 >> y2;
    long int x = abs(x1 - x2);
    long int y = abs(y1 - y2);
    cout << euclidean_algorithm(x, y) - 1 << endl;
    return 0;
}