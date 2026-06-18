// Pythonからの翻訳
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<pair<long long, long long>> change(M); // (C, B)
    for (int i = 0; i < M; ++i) {
        long long B, C;
        cin >> B >> C;
        change[i] = {C, B};
    }

    sort(change.begin(), change.end()); // 小さい順なので、あとで後ろから使う

    vector<long long> card;
    int cnt = 0;
    while (!change.empty()) {
        auto [c, b] = change.back();
        change.pop_back();
        if (cnt + b < N) {
            for (int i = 0; i < b; ++i) {
                card.push_back(c);
            }
            cnt += b;
        } else {
            for (int i = 0; i < N - cnt; ++i) {
                card.push_back(c);
            }
            break;
        }
    }

    vector<long long> X = A;
    X.insert(X.end(), card.begin(), card.end());

    sort(X.begin(), X.end(), greater<long long>());

    long long result = 0;
    for (int i = 0; i < N; ++i) {
        result += X[i];
    }

    cout << result << endl;
    return 0;
}
