// Pythonからの翻訳
#include <bits/stdc++.h>
#include <atcoder/dsu>
using namespace std;
using namespace atcoder;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    dsu g(N + 1);
    vector<set<int>> friend_rel(N + 1);
    vector<set<int>> block_rel(N + 1);

    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        g.merge(A, B);
        friend_rel[A].insert(B);
        friend_rel[B].insert(A);
    }

    for (int i = 0; i < K; i++) {
        int C, D;
        cin >> C >> D;
        block_rel[C].insert(D);
        block_rel[D].insert(C);
    }

    vector<int> pre(N + 1, 0);
    vector<vector<int>> groups = g.groups();

    for (const auto& G : groups) {
        set<int> Gset(G.begin(), G.end());
        for (int m : G) {
            int cnt = Gset.size();
            for (int f : friend_rel[m]) if (Gset.count(f)) cnt--;
            for (int b : block_rel[m])  if (Gset.count(b)) cnt--;
            pre[m] = cnt - 1;  // 自分自身を除く
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << pre[i] << " ";
    }
    cout << endl;

    return 0;
}
