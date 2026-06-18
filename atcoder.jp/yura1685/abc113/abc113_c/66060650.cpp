#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<pair<int, int>> city(M);
    vector<vector<int>> x(N + 1);
    vector<int> e;

    for (int i = 0; i < M; ++i) {
        int p, y;
        cin >> p >> y;
        city[i] = {p, y};
        x[p].push_back(y);
        e.push_back(p);
    }

    map<pair<int, int>, string> d;

    for (int i = 1; i <= N; ++i) {
        sort(x[i].begin(), x[i].end());
        for (int j = 0; j < x[i].size(); ++j) {
            ostringstream oss;
            oss << setw(6) << setfill('0') << i;
            oss << setw(6) << setfill('0') << j + 1;
            d[{i, x[i][j]}] = oss.str();
        }
    }

    for (auto& [u, r] : city) {
        cout << d[{u, r}] << endl;
    }

    return 0;
}
