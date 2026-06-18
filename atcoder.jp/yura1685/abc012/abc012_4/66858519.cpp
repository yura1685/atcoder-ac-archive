#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<pair<int, int>>> g(N);
    for (int i = 0; i < M; ++i) {
        int a, b, t;
        cin >> a >> b >> t;
        --a; --b;
        g[a].emplace_back(b, t);
        g[b].emplace_back(a, t);
    }

    int ans = INT_MAX;

    for (int st = 0; st < N; ++st) {
        vector<int> dist(N, INT_MAX);
        dist[st] = 0;

        vector<int> d = {st};
        vector<pair<int, int>> hoge;

        while (!d.empty()) {
            int u = d.back(); d.pop_back();
            for (auto [v, t] : g[u]) {
                if (dist[v] > dist[u] + t) {
                    dist[v] = dist[u] + t;
                    hoge.emplace_back(dist[v], v);
                }
            }

            if (!hoge.empty()) {
                sort(hoge.rbegin(), hoge.rend()); // 降順ソート
                auto [cost, v] = hoge.back(); hoge.pop_back();
                d.push_back(v);
            }
        }

        int max_dist = *max_element(dist.begin(), dist.end());
        ans = min(ans, max_dist);
    }

    cout << ans << endl;
    return 0;
}
