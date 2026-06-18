#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K, N;
    cin >> R >> C >> K >> N;

    vector<int> Rc(R + 1, 0), Cc(C + 1, 0);
    vector<pair<int, int>> items(N);

    for (int i = 0; i < N; ++i) {
        cin >> items[i].first >> items[i].second;
        Rc[items[i].first]++;
        Cc[items[i].second]++;
    }

    vector<long long> cntR(N + 1, 0), cntC(N + 1, 0);
    for (int r = 1; r <= R; ++r) if (Rc[r] <= N) cntR[Rc[r]]++;
    for (int c = 1; c <= C; ++c) if (Cc[c] <= N) cntC[Cc[c]]++;

    long long ans = 0;
    for (int i = 0; i <= K; ++i) {
        if (i <= N && (K - i) >= 0 && (K - i) <= N) {
            ans += cntR[i] * cntC[K - i];
        }
    }

    for (int i = 0; i < N; ++i) {
        int r = items[i].first;
        int c = items[i].second;
        int total = Rc[r] + Cc[c];

        if (total == K) {
            ans--;
        } else if (total == K + 1) {
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}