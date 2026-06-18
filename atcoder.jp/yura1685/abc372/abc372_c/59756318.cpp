#include <iostream>
#include <vector>
#include <string>

using namespace std;

// check関数: 文字列中の "ABC" の出現回数を数える
int check(const string &x) {
    int abc = 0;
    for (size_t i = 0; i + 2 < x.size(); i++) {
        if (x.substr(i, 3) == "ABC") {
            abc++;
        }
    }
    return abc;
}

int main() {
    int N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    vector<int> c(N, 0);

    // 初期カウント
    int ans = 0;
    for (int i = 0; i < N - 2; i++) {
        if (S.substr(i, 3) == "ABC") {
            c[i] = 1;
            ans++;
        }
    }

    for (int i = 0; i < Q; i++) {
        int n;
        char s;
        cin >> n >> s;
        n--; // 0-based indexingに変換

        // 元の "ABC" パターンを ans から引く
        if (n > 1 && S.substr(n - 2, 3) == "ABC") ans--;
        if (n > 0 && n < N - 1 && S.substr(n - 1, 3) == "ABC") ans--;
        if (n < N - 2 && S.substr(n, 3) == "ABC") ans--;

        // 文字列を更新
        S[n] = s;

        // 更新後の "ABC" パターンを ans に加える
        if (n > 1 && S.substr(n - 2, 3) == "ABC") ans++;
        if (n > 0 && n < N - 1 && S.substr(n - 1, 3) == "ABC") ans++;
        if (n < N - 2 && S.substr(n, 3) == "ABC") ans++;

        cout << ans << endl;
    }

    return 0;
}
