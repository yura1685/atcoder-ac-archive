#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

vector<int> bfs(int n, const vector<vector<int>>& g,
                const vector<pair<int, int>>& sources) {
  vector<int> dist(n, 1e9);
  vector<vector<int>> bucket(n + 1);
  for (auto [v, d] : sources) {
    assert(-n <= d && d <= 0);
    dist[v] = d;
    bucket[n + d].push_back(v);
  }
  queue<int> que_init, que_bfs;
  rep(i, n + 1) for (int v : bucket[i]) que_init.push(v);
  vector<char> visited(n);
  while (!que_init.empty() || !que_bfs.empty()) {
    int u;
    if (!que_init.empty() &&
        (que_bfs.empty() || dist[que_init.front()] < dist[que_bfs.front()])) {
      u = que_init.front();
      que_init.pop();
    } else {
      u = que_bfs.front();
      que_bfs.pop();
    }
    if (visited[u]) continue;
    visited[u] = true;
    for (int v : g[u]) {
      if (dist[u] + 1 < dist[v]) {
        dist[v] = dist[u] + 1;
        que_bfs.push(v);
      }
    }
  }
  return dist;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> g(n);
  rep(_, m) {
    int u, v;
    cin >> u >> v;
    u--, v--;
    g[u].emplace_back(v);
    g[v].emplace_back(u);
  }
  int k;
  cin >> k;
  vector<pair<int, int>> pd(k);
  for (auto& [p, d] : pd) {
    cin >> p >> d;
    p--;
    d *= -1;
  }
  vector<int> t = bfs(n, g, pd);
  vector<pair<int, int>> blacks;
  rep(i, n) if (t[i] >= 0) blacks.emplace_back(i, 0);
  vector<int> dist = bfs(n, g, blacks);
  for (auto [p, d] : pd) {
    if (dist[p] != -d) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
  string ans;
  rep(i, n) ans += t[i] < 0 ? '0' : '1';
  cout << ans << endl;
}