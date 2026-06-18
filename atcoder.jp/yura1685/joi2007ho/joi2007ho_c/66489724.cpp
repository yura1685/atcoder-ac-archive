#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

// 二分探索で存在確認
bool exists(const vector<pair<int, int>>& post, pair<int, int> p) {
    auto it = lower_bound(post.begin(), post.end(), p);
    return it != post.end() && *it == p;
}

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> post(n);

    for (int i = 0; i < n; ++i) {
        cin >> post[i].first >> post[i].second;
    }

    sort(post.begin(), post.end());

    int ans = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int x1 = post[i].first, y1 = post[i].second;
            int x2 = post[j].first, y2 = post[j].second;

            // 対角線が(x1,y1)-(x2,y2)である正方形の残り2点を計算
            // 座標は整数になるように調整
            int x3_num = x1 - y1 + x2 + y2;
            int y3_num = x1 + y1 - x2 + y2;
            int x4_num = x1 + y1 + x2 - y2;
            int y4_num = -x1 + y1 + x2 + y2;

            if (x3_num % 2 != 0 || y3_num % 2 != 0 || x4_num % 2 != 0 || y4_num % 2 != 0) continue;

            pair<int, int> p3 = {x3_num / 2, y3_num / 2};
            pair<int, int> p4 = {x4_num / 2, y4_num / 2};

            if (exists(post, p3) && exists(post, p4)) {
                int dx = x2 - x1, dy = y2 - y1;
                int area = (dx * dx + dy * dy) / 2;
                ans = max(ans, area);
            }
        }
    }

    cout << ans << endl;
    return 0;
}
