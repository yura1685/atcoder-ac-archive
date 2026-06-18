#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> G(H);
    for (int i = 0; i < H; i++) {
        cin >> G[i];
    }

    int now_h = 0, now_w = 0;
    set<pair<int, int>> visit;
    visit.insert({0, 0});

    while (true) {
        if (G[now_h][now_w] == 'R' && now_w == W - 1) {
            cout << now_h + 1 << " " << now_w + 1 << endl;
            return 0;
        }
        if (G[now_h][now_w] == 'R' && now_w != W - 1) {
            now_w += 1;
            if (visit.count({now_h, now_w})) {
                cout << -1 << endl;
                return 0;
            } else {
                visit.insert({now_h, now_w});
            }
        }

        if (G[now_h][now_w] == 'U' && now_h == 0) {
            cout << now_h + 1 << " " << now_w + 1 << endl;
            return 0;
        }
        if (G[now_h][now_w] == 'U' && now_h != 0) {
            now_h -= 1;
            if (visit.count({now_h, now_w})) {
                cout << -1 << endl;
                return 0;
            } else {
                visit.insert({now_h, now_w});
            }
        }

        if (G[now_h][now_w] == 'L' && now_w == 0) {
            cout << now_h + 1 << " " << now_w + 1 << endl;
            return 0;
        }
        if (G[now_h][now_w] == 'L' && now_w != 0) {
            now_w -= 1;
            if (visit.count({now_h, now_w})) {
                cout << -1 << endl;
                return 0;
            } else {
                visit.insert({now_h, now_w});
            }
        }

        if (G[now_h][now_w] == 'D' && now_h == H - 1) {
            cout << now_h + 1 << " " << now_w + 1 << endl;
            return 0;
        }
        if (G[now_h][now_w] == 'D' && now_h != H - 1) {
            now_h += 1;
            if (visit.count({now_h, now_w})) {
                cout << -1 << endl;
                return 0;
            } else {
                visit.insert({now_h, now_w});
            }
        }
    }
}
