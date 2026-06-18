#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    unordered_map<int, int> num_map;
    vector<int> B(N);

    for (int i = 0; i < N; ++i) {
        if (num_map.find(A[i]) != num_map.end()) {
            B[i] = num_map[A[i]];
            num_map[A[i]] = i + 1;
        } else {
            B[i] = -1;
            num_map[A[i]] = i + 1;
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << B[i] << " ";
    }
    cout << endl;

    return 0;
}
