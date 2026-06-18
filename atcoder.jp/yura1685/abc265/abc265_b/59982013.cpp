#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    long long T; // 時間をlong longに変更
    cin >> N >> M >> T;

    vector<long long> A(N - 1); // Aもlong long型に変更
    for (int i = 0; i < N - 1; i++) {
        cin >> A[i];
    }

    vector<int> x(M);
    vector<long long> y(M); // ボーナスもlong long型に変更
    for (int i = 0; i < M; i++) {
        cin >> x[i] >> y[i];
    }

    int now = 1;
    while (now != N) {
        // ボーナスのチェック
        for (int i = 0; i < M; i++) {
            if (x[i] == now) {
                T += y[i];
                break;
            }
        }

        if (T <= A[now - 1]) {
            cout << "No" << endl;
            return 0;
        }

        T -= A[now - 1];
        now++;
    }

    cout << "Yes" << endl;
    return 0;
}
