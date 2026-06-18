#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

// グローバル変数でキャッシュとして使う
set<string> cache;

bool is_palindrome(const string& x, int K) {
    if (cache.count(x)) return true;
    for (int i = 0; i < K / 2; ++i) {
        if (x[i] != x[K - 1 - i]) return false;
    }
    cache.insert(x);
    return true;
}

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    sort(S.begin(), S.end()); // permutationsを使う前にソートが必要
    set<string> ans;

    do {
        bool found = false;
        for (int i = 0; i <= N - K; ++i) {
            if (S[i] == S[i + K - 1]) {
                string sub = S.substr(i, K);
                if (is_palindrome(sub, K)) {
                    found = true;
                    break;
                }
            }
        }
        if (!found) ans.insert(S);
    } while (next_permutation(S.begin(), S.end()));

    cout << ans.size() << endl;
    return 0;
}
