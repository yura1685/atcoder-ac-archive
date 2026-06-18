// Pythonからの翻訳

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> yen(N);
    for (int i = 0; i < N; ++i) cin >> yen[i];

    vector<vector<int>> park(N);
    for (int i = 0; i < M; ++i) {
        int k;
        cin >> k;
        for (int j = 0; j < k; ++j) {
            int p;
            cin >> p;
            park[p - 1].push_back(i);
        }
    }

    long long ans = LLONG_MAX;

    for (int b1 = 0; b1 < (1 << N); ++b1) {
        for (int b2 = 0; b2 < (1 << N); ++b2) {
            vector<int> A(M, 0);
            long long hoge = 0;
            for (int i = 0; i < N; ++i) {
                if (b1 & (1 << i)) {
                    hoge += yen[i];
                    for (int p : park[i]) {
                        A[p]++;
                    }
                }
                if (b2 & (1 << i)) {
                    hoge += yen[i];
                    for (int p : park[i]) {
                        A[p]++;
                    }
                }
            }
            bool ok = true;
            for (int x : A) {
                if (x < 2) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans = min(ans, hoge);
            }
        }
    }

    cout << ans << endl;

    return 0;
}
