#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
using namespace std;

// Pythonからの翻訳
bool f(const vector<vector<int>>& L) {
    // 行チェック
    for (int i = 0; i < 3; ++i) {
        set<int> s(L[i].begin(), L[i].end());
        if (s.size() == 2) {
            int sum = accumulate(L[i].begin(), L[i].end(), 0);
            if (sum < 0) return false;
        }
    }

    // 列チェック
    for (int j = 0; j < 3; ++j) {
        set<int> s = {L[0][j], L[1][j], L[2][j]};
        if (s.size() == 2) {
            int sum = L[0][j] + L[1][j] + L[2][j];
            if (sum < 0) return false;
        }
    }

    // 斜めチェック
    set<int> s1 = {L[0][0], L[1][1], L[2][2]};
    if (s1.size() == 2 && (L[0][0] + L[1][1] + L[2][2] < 0)) return false;

    set<int> s2 = {L[0][2], L[1][1], L[2][0]};
    if (s2.size() == 2 && (L[0][2] + L[1][1] + L[2][0] < 0)) return false;

    return true;
}

int main() {
    vector<vector<int>> c(3, vector<int>(3));
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            cin >> c[i][j];

    vector<int> x(9);
    iota(x.begin(), x.end(), 0);  // 0〜8

    int ans = 0;
    do {
        vector<vector<int>> d = {
            {-21, -22, -23},
            {-24, -25, -26},
            {-27, -28, -29}
        };

        for (int k = 0; k < 9; ++k) {
            int a = x[k] / 3;
            int b = x[k] % 3;
            d[a][b] = c[a][b];
            if (!f(d)) {
                ans += 1;
                break;
            }
        }
    } while (next_permutation(x.begin(), x.end()));

    cout.precision(10);
    cout << 1.0 - static_cast<double>(ans) / 362880.0 << endl;
    return 0;
}
