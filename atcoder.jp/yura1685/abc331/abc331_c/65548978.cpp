#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    vector<int> B = A;
    sort(B.begin(), B.end());

    // C = sorted(set(A))
    vector<int> C = A;
    sort(C.begin(), C.end());
    C.erase(unique(C.begin(), C.end()), C.end());

    map<int, long long> S;

    for (int i = 0; i < (int)C.size(); ++i) {
        int x = C[C.size() - 1 - i];
        if (i == 0) {
            S[x] = 0;
        } else {
            int y = C[C.size() - i];
            // bisect.bisect and bisect.bisect_left
            auto upper = upper_bound(B.begin(), B.end(), y);
            auto lower = lower_bound(B.begin(), B.end(), y);
            int count = upper - lower;
            S[x] = S[y] + 1LL * y * count;
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << S[A[i]];
        if (i != N - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
