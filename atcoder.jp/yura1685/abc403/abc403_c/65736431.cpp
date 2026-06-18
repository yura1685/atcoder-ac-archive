#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    int N, M, Q;
    cin >> N >> M >> Q;

    unordered_map<int, vector<int>> page;
    unordered_set<int> approved;

    for (int query = 0; query < Q; ++query) {
        int q;
        cin >> q;

        if (q == 1) {
            int man, p;
            cin >> man >> p;
            page[p].push_back(man);
        } else if (q == 2) {
            int man;
            cin >> man;
            approved.insert(man);
        } else {
            int man, p;
            cin >> man >> p;

            if (approved.count(man)) {
                cout << "Yes" << endl;
            } else {
                if (page.find(p) == page.end()) {
                    cout << "No" << endl;
                } else {
                    bool found = false;
                    for (int m : page[p]) {
                        if (m == man) {
                            found = true;
                            break;
                        }
                    }
                    if (found) {
                        cout << "Yes" << endl;
                    } else {
                        cout << "No" << endl;
                    }
                }
            }
        }
    }

    return 0;
}
