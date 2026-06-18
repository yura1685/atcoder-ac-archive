#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

double distance(const vector<int>& a, const vector<int>& b) {
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2));
}

int main() {
    int N, D;
    cin >> N >> D;

    vector<vector<int>> points(N, vector<int>(2));
    for (int i = 0; i < N; ++i) {
        cin >> points[i][0] >> points[i][1];
    }

    vector<int> virus(N, 0);
    virus[0] = 1;

    queue<int> check;
    check.push(0);

    while (!check.empty()) {
        int current = check.front();
        check.pop();

        for (int i = 0; i < N; ++i) {
            if (distance(points[current], points[i]) <= D) {
                if (virus[i] == 0) {
                    virus[i] = 1;
                    check.push(i);
                }
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        if (virus[i] == 1) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }

    return 0;
}
