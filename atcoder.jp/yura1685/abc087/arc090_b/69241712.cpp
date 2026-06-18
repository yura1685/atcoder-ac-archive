#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <stack>
#include <algorithm>

#include <atcoder/dsu>

using namespace std;
using namespace atcoder;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    dsu uf(N);
    vector<vector<pair<int, int>>> dd(N);
    for (int i = 0; i < M; ++i) {
        int L, R, D;
        cin >> L >> R >> D;
        --L; --R;
        uf.merge(L, R);
        dd[L].push_back({R, D});
        dd[R].push_back({L, -D});
    }

    auto groups = uf.groups();

    for (const auto& group : groups) {
        if (group.size() == 1) {
            continue;
        }

        map<int, long long> dic;
        bool possible = true;

        for (int u : group) {
            if (dic.count(u)) {
                continue;
            }

            dic[u] = 0; // 基準点を0として設定
            stack<int> s;
            s.push(u);

            while (!s.empty()) {
                int curr = s.top();
                s.pop();

                for (const auto& edge : dd[curr]) {
                    int neighbor = edge.first;
                    long long dist = edge.second;
                    
                    if (!dic.count(neighbor)) {
                        dic[neighbor] = dic[curr] + dist;
                        s.push(neighbor);
                    } else if (dic[neighbor] != dic[curr] + dist) {
                        possible = false;
                        break;
                    }
                }
                if (!possible) break;
            }
            if (!possible) break;
        }
        
        if (!possible) {
            cout << "No" << endl;
            return 0;
        }

        if (!dic.empty()) {
            long long min_val = dic.begin()->second;
            long long max_val = dic.begin()->second;
            for (const auto& pair : dic) {
                min_val = min(min_val, pair.second);
                max_val = max(max_val, pair.second);
            }

            if (max_val - min_val > 1000000000LL) {
                cout << "No" << endl;
                return 0;
            }
        }
    }

    cout << "Yes" << endl;

    return 0;
}