#include <iostream>
#include <vector>
using namespace std;

const int MAX = 200005;
vector<int> g[MAX];
long long counter[MAX];
bool check[MAX];

void dfs(int u, long long cnt) {
    for (int v : g[u]) {
        if (!check[v]) {
            check[v] = true;
            counter[v] += cnt;
            dfs(v, counter[v]);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    for (int i = 0; i < Q; ++i) {
        int p;
        long long x;
        cin >> p >> x;
        counter[p] += x;
    }

    check[1] = true;
    dfs(1, counter[1]);

    for (int i = 1; i <= N; ++i) {
        cout << counter[i] << (i == N ? '\n' : ' ');
    }

    return 0;
}
