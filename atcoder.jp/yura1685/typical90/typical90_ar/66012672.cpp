/*
from collections import deque

N , Q = map(int,input().split())
A = deque(map(int,input().split()))

for _ in range(Q):
    T, x, y = map(int,input().split())
    if T == 1:
        A[x-1], A[y-1] = A[y-1], A[x-1]
    elif T == 2:
        hoge = A.pop()
        A.appendleft(hoge)
    else:
        print(A[x-1])
*/

#include <iostream>
#include <deque>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    deque<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    for (int i = 0; i < Q; ++i) {
        int T, x, y;
        cin >> T >> x >> y;

        if (T == 1) {
            swap(A[x - 1], A[y - 1]);
        } else if (T == 2) {
            int hoge = A.back();
            A.pop_back();
            A.push_front(hoge);
        } else {
            cout << A[x - 1] << endl;
        }
    }

    return 0;
}
