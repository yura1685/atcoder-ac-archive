// Pythonからの翻訳
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <sstream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<pair<int64_t, int64_t>>> num;
    unordered_map<int64_t, pair<int64_t, int64_t>> d;

    for (int i = 0; i < N; ++i) {
        int m;
        cin >> m;
        vector<pair<int64_t, int64_t>> X;
        for (int j = 0; j < m; ++j) {
            int64_t p, e;
            cin >> p >> e;
            if (d.find(p) == d.end()) {
                d[p] = {0, e};
            } else if (d[p].first < e && e <= d[p].second) {
                d[p].first = e;
            } else if (d[p].second <= e) {
                d[p].first = d[p].second;
                d[p].second = e;
            }
            X.push_back({p, e});
        }
        num.push_back(X);
    }

    set<string> s;

    for (const auto& lst : num) {
        ostringstream oss;
        for (const auto& [p, e] : lst) {
            if (d[p].first < e) {
                oss << "-" << p;
            }
        }
        s.insert(oss.str());
    }

    cout << s.size() << endl;
    return 0;
}
