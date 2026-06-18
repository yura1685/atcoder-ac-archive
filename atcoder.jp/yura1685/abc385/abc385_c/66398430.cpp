#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

int f(const vector<int>& L) {
    int n = L.size();
    int ans = 1;
    unordered_set<int> S(L.begin(), L.end());
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int cnt = 2;
            int a1 = L[i];
            int a2 = L[j];
            int sa = a2 - a1;
            int next = a2 + sa;
            while (S.count(next)) {
                ++cnt;
                next += sa;
            }
            ans = max(ans, cnt);
        }
    }
    return ans;
}

int main() {
    int N;
    cin >> N;
    vector<int> H(N);
    for (int i = 0; i < N; ++i) {
        cin >> H[i];
    }

    int maxH = *max_element(H.begin(), H.end());
    vector<vector<int>> build(maxH + 1);
    for (int i = 0; i < N; ++i) {
        int h = H[i];
        build[h].push_back(i);
    }

    int ans = 0;
    for (const auto& b : build) {
        if (!b.empty()) {
            ans = max(ans, f(b));
        }
    }

    cout << ans << endl;
    return 0;
}
