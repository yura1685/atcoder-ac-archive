#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const long long INF = 1e18;

int N, M;
vector<vector<pair<int, long long>>> graph;
vector<long long> x;

void dfs(int u) {
    for (auto [v, w] : graph[u]) {
        if (x[v] == INF) {
            x[v] = x[u] + w;
            dfs(v);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.resize(N);
    x.assign(N, INF);

    for (int i = 0; i < M; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        --u; --v;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, -w);
    }

    for (int i = 0; i < N; ++i) {
        if (x[i] == INF) {
            x[i] = 0;
            dfs(i);
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << x[i];
        if (i != N - 1) cout << ' ';
    }
    cout << '\n';

    return 0;
}
