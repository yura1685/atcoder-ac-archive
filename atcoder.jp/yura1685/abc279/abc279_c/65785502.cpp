/*
H, W = map(int,input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
Sq, Tq = [], []
for w in range(W):
    x, y = '', ''
    for h in range(H):
        x += S[h][w]
        y += T[h][w]
    Sq.append(x)
    Tq.append(y)
Sq.sort(); Tq.sort()
if Sq == Tq:
    print('Yes')
else:
    print('No')
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> S(H), T(H);
    for (int i = 0; i < H; ++i) cin >> S[i];
    for (int i = 0; i < H; ++i) cin >> T[i];

    vector<string> Sq, Tq;
    for (int w = 0; w < W; ++w) {
        string x = "", y = "";
        for (int h = 0; h < H; ++h) {
            x += S[h][w];
            y += T[h][w];
        }
        Sq.push_back(x);
        Tq.push_back(y);
    }

    sort(Sq.begin(), Sq.end());
    sort(Tq.begin(), Tq.end());

    if (Sq == Tq) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}
