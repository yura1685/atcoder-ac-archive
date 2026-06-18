// Pythonからの翻訳

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

const int MAX = 200005;
vector<int> g[MAX];
bool visited[MAX];
int parent[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, X, Y;
    cin >> N >> X >> Y;

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    stack<int> s;
    s.push(X);
    visited[X] = true;
    parent[X] = -1;

    // DFS to find path from X to Y
    while (!s.empty()) {
        int u = s.top();
        s.pop();
        for (int v : g[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                s.push(v);
            }
        }
    }

    // Reconstruct the path from X to Y using parent[]
    vector<int> path;
    for (int cur = Y; cur != -1; cur = parent[cur]) {
        path.push_back(cur);
    }

    // Reverse the path to go from X to Y
    for (int i = path.size() - 1; i >= 0; --i) {
        cout << path[i] << " ";
    }
    cout << '\n';

    return 0;
}
