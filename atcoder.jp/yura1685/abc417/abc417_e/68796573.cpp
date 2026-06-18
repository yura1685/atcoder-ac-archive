// Pythonからの翻訳であることに注意されたい
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N, M, X, Y;
    cin >> N >> M >> X >> Y;

    vector<vector<int>> g(N + 1);
    vector<vector<int>> m(N + 1, vector<int>(1, INT_MAX)); // 各頂点の最小経路
    m[X] = {X};

    for (int i = 0; i < M; i++) {
        int U, V;
        cin >> U >> V;
        g[U].push_back(V);
        g[V].push_back(U);
    }

    // set: (経路ベクトル, 経路の末端)
    auto cmp = [](const vector<int>& a, const vector<int>& b) {
        return a < b; // 辞書順比較
    };
    set<vector<int>, decltype(cmp)> SL(cmp);

    SL.insert({X});

    while (!SL.empty()) {
        auto lst = *SL.begin();
        SL.erase(SL.begin());

        int u = lst.back();
        if (u == Y) {
            for (int i = 0; i < (int)m[Y].size(); i++) {
                if (i) cout << " ";
                cout << m[Y][i];
            }
            cout << "\n";
            return;
        }

        for (int v : g[u]) {
            vector<int> nxt = lst;
            nxt.push_back(v);
            if (nxt < m[v]) {
                if (m[v][0] != INT_MAX) SL.erase(m[v]); // 古い経路を削除
                m[v] = nxt;
                SL.insert(nxt);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) solve();
}
