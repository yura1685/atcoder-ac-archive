#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

vector<vector<char>> narabikae(vector<char> L) {
    vector<vector<char>> res;
    sort(L.begin(), L.end());
    do {
        res.push_back(L);
    } while (next_permutation(L.begin(), L.end()));
    return res;
}

int main() {
    int H, W;
    cin >> H >> W;

    vector<vector<int>> A(H, vector<int>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> A[i][j];
        }
    }

    vector<char> L;
    for (int i = 0; i < H - 1; i++) L.push_back('h');
    for (int i = 0; i < W - 1; i++) L.push_back('w');

    vector<vector<char>> x = narabikae(L);

    int ans = 0;
    for (auto pat : x) {
        int x = 0, y = 0;
        set<int> l;
        l.insert(A[0][0]);
        for (char i : pat) {
            if (i == 'h') {
                x += 1;
            } else {
                y += 1;
            }
            l.insert(A[x][y]);
        }
        if ((int)l.size() == H + W - 1) {
            ans += 1;
        }
    }

    cout << ans << endl;

    return 0;
}
