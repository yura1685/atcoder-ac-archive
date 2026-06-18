#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int H, W;
vector<vector<int>> g;

int dfs(vector<vector<int>> graph, int x, int y, int depth) {
    int ret = depth;
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};

    graph[x][y] = 0; // 訪問済みにする

    for (int d = 0; d < 4; ++d) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (graph[nx][ny] == 1) {
            int hoge = dfs(graph, nx, ny, depth + 1);
            ret = max(ret, hoge);
        }
    }

    return ret;
}

int main() {
    cin >> W >> H;
    g = vector<vector<int>>(H + 2, vector<int>(W + 2, 0));

    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            cin >> g[i][j];
        }
    }

    int ans = 0;
    for (int i = 1; i <= H; ++i) {
        for (int j = 1; j <= W; ++j) {
            if (g[i][j] == 1) {
                ans = max(ans, dfs(g, i, j, 1));
            }
        }
    }

    cout << ans << endl;
    return 0;
}
