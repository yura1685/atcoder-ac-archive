#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 1000005;

vector<int> g[MAX];

int leave(int u, int from) {
    if (g[u].size() == 1) {
        return 1;
    }
    int ans = 0;
    for (int v : g[u]) {
        if (v != from) {
            ans += leave(v, u);
        }
    }
    return ans + 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    vector<int> hoge;
    for (int v : g[1]) {
        hoge.push_back(leave(v, 1));
    }

    sort(hoge.begin(), hoge.end());

    int ans = 0;
    for (int i = 0; i < (int)hoge.size() - 1; ++i) {
        ans += hoge[i];
    }

    cout << ans + 1 << '\n';

    return 0;
}
