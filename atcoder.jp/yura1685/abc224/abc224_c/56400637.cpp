#include <iostream>
#include <vector>
#include <cmath> // abs関数を使うために必要

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> X(N), Y(N);
    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
    }
    
    int ans = 0;
    
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            for (int k = j + 1; k < N; ++k) {
                int x1 = X[i], y1 = Y[i];
                int x2 = X[j], y2 = Y[j];
                int x3 = X[k], y3 = Y[k];
                
                int area = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);
                if (abs(area) != 0) {
                    ++ans;
                }
            }
        }
    }
    
    cout << ans << endl;
    return 0;
}
