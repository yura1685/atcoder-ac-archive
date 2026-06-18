#include <iostream>
#include <vector>
#include <numeric>
#include <random>
#include <queue>
#include <limits>

using namespace std;

// 再帰呼び出しの上限を増やす（通常は不要だが、Pythonコードに合わせて記述）
// C++ではデフォルトのスタックサイズが大きいため、通常はsetrecursionlimitは不要
// ただし、非常に深い再帰が必要な場合は、コンパイラや環境に依存した方法でスタックサイズを増やす必要がある

int N;
vector<vector<int>> g;
vector<int> up;
vector<long long> C;
vector<long long> sum_tree;
vector<long long> anslist;

// DFSを用いて部分木の合計値を計算する
long long dfs(int u) {
    long long res = C[u];
    for (int v : g[u]) {
        if (v == up[u]) {
            continue;
        }
        res += dfs(v);
    }
    sum_tree[u] = res;
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    g.resize(N);
    up.assign(N, -1);
    C.resize(N);
    sum_tree.assign(N, 0);
    anslist.assign(N, -1);

    // 乱数生成器
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, N - 1);
    int p = dis(gen);

    for (int i = 0; i < N - 1; ++i) {
        int A, B;
        cin >> A >> B;
        g[A - 1].push_back(B - 1);
        g[B - 1].push_back(A - 1);
    }

    for (int i = 0; i < N; ++i) {
        cin >> C[i];
    }
    long long S = accumulate(C.begin(), C.end(), 0LL);

    // BFSで親ノード(up)を決定する
    up[p] = p;
    queue<int> q;
    q.push(p);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (up[v] >= 0) {
                continue;
            }
            up[v] = u;
            q.push(v);
        }
    }

    // DFSで部分木の合計値を計算する
    dfs(p);

    // BFSで最初のノード(p)からの距離と重み付きパスの合計を計算する
    long long ans = 0;
    queue<pair<int, int>> q2;
    q2.push({p, 0});
    while (!q2.empty()) {
        pair<int, int> current = q2.front();
        q2.pop();
        int u = current.first;
        int depth = current.second;
        ans += C[u] * depth;
        for (int v : g[u]) {
            if (v == up[u]) {
                continue;
            }
            q2.push({v, depth + 1});
        }
    }
    anslist[p] = ans;

    // 根を一つずつ移動させながら、重み付きパスの合計を再計算する
    // これは「全方位木DP」と呼ばれるアルゴリズム
    queue<int> q3;
    q3.push(p);
    vector<bool> visited(N, false);
    visited[p] = true;

    while (!q3.empty()) {
        int u = q3.front();
        q3.pop();
        
        for (int v : g[u]) {
            if (v != up[u]) { // 子ノードの場合
                anslist[v] = anslist[u] - sum_tree[v] + (S - sum_tree[v]);
                q3.push(v);
            }
        }
    }

    // 最小値を見つける
    long long min_val = numeric_limits<long long>::max();
    for (int i = 0; i < N; ++i) {
        min_val = min(min_val, anslist[i]);
    }

    cout << min_val << endl;

    return 0;
}