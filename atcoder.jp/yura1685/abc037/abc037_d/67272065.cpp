// Pythonからの翻訳
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    int H, W;
    cin >> H >> W;

    vector<vector<int>> glid(H + 2, vector<int>(W + 2, 0));
    for (int h = 1; h <= H; ++h) {
        for (int w = 1; w <= W; ++w) {
            cin >> glid[h][w];
        }
    }

    vector<tuple<int, int, int>> num;
    for (int h = 1; h <= H; ++h) {
        for (int w = 1; w <= W; ++w) {
            num.emplace_back(glid[h][w], h, w);
        }
    }

    // 降順ソート
    sort(num.rbegin(), num.rend());

    vector<vector<int>> ans(H + 2, vector<int>(W + 2, 0));
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};

    for (auto& [n, h, w] : num) {
        ans[h][w] = 1;
        for (int dir = 0; dir < 4; ++dir) {
            int nh = h + dx[dir], nw = w + dy[dir];
            if (glid[nh][nw] > glid[h][w]) {
                ans[h][w] += ans[nh][nw];
                if (ans[h][w] >= MOD) ans[h][w] -= MOD;
            }
        }
    }

    int total = 0;
    for (int h = 1; h <= H; ++h) {
        for (int w = 1; w <= W; ++w) {
            total = (total + ans[h][w]) % MOD;
        }
    }

    cout << total << endl;
    return 0;
}
