/*
from itertools import product

N, K, X = map(int,input().split())
S = [input() for _ in range(N)]

lst = []
for P in product((i for i in range(N)),repeat=K):
    f = ''
    for p in P:
        f += S[p]
    lst.append(f)

lst.sort()
print(lst[X-1])
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int N, K, X;
    cin >> N >> K >> X;
    vector<string> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    vector<string> lst;

    // Pythonのproduct(range(N), repeat=K)を整数の進数として模倣
    long long total = 1;
    for (int i = 0; i < K; ++i) total *= N;

    for (long long t = 0; t < total; ++t) {
        vector<int> P(K);
        long long tmp = t;
        for (int i = K - 1; i >= 0; --i) {
            P[i] = tmp % N;
            tmp /= N;
        }

        string f = "";
        for (int i = 0; i < K; ++i) {
            f += S[P[i]];
        }
        lst.push_back(f);
    }

    sort(lst.begin(), lst.end());

    cout << lst[X - 1] << endl;

    return 0;
}
