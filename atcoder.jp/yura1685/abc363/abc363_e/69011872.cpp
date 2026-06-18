#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

// 高さを基準にソートするための構造体
struct Element {
    int height;
    int h, w;

    bool operator>(const Element& other) const {
        return height > other.height;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W, Y;
    cin >> H >> W >> Y;

    vector<vector<int>> A(H, vector<int>(W));
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> A[i][j];
        }
    }

    vector<vector<bool>> visited(H, vector<bool>(W, false));
    priority_queue<Element, vector<Element>, greater<Element>> pq;

    // 外側の境界を初期化
    for (int w = 0; w < W; ++w) {
        pq.push({A[0][w], 0, w});
        visited[0][w] = true;
        if (H > 1) {
            pq.push({A[H - 1][w], H - 1, w});
            visited[H - 1][w] = true;
        }
    }
    for (int h = 1; h < H - 1; ++h) {
        pq.push({A[h][0], h, 0});
        visited[h][0] = true;
        if (W > 1) {
            pq.push({A[h][W - 1], h, W - 1});
            visited[h][W - 1] = true;
        }
    }

    long long island = (long long)H * W;
    int dh[] = {-1, 0, 0, 1};
    int dw[] = {0, -1, 1, 0};

    for (int i = 1; i <= Y; ++i) {
        while (!pq.empty() && pq.top().height <= i) {
            Element current = pq.top();
            pq.pop();

            island--;

            for (int k = 0; k < 4; ++k) {
                int nh = current.h + dh[k];
                int nw = current.w + dw[k];

                if (nh >= 0 && nh < H && nw >= 0 && nw < W && !visited[nh][nw]) {
                    pq.push({A[nh][nw], nh, nw});
                    visited[nh][nw] = true;
                }
            }
        }
        cout << island << endl;
    }

    return 0;
}