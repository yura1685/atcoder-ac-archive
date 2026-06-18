#include <iostream>
#include <vector>
using namespace std;

int main() {
    int H, W, K;
    cin >> H >> W;
    cin >> K;

    vector<vector<char>> iceland(H + 1, vector<char>(W + 1, '#'));
    for (int h = 1; h <= H; ++h) {
        for (int w = 1; w <= W; ++w) {
            cin >> iceland[h][w];
        }
    }

    vector<vector<int>> Ja(H + 1, vector<int>(W + 1, 0));
    vector<vector<int>> Oc(H + 1, vector<int>(W + 1, 0));
    vector<vector<int>> Ic(H + 1, vector<int>(W + 1, 0));

    for (int h = 1; h <= H; ++h) {
        for (int w = 1; w <= W; ++w) {
            Ja[h][w] = Ja[h-1][w] + Ja[h][w-1] - Ja[h-1][w-1] + (iceland[h][w] == 'J');
            Oc[h][w] = Oc[h-1][w] + Oc[h][w-1] - Oc[h-1][w-1] + (iceland[h][w] == 'O');
            Ic[h][w] = Ic[h-1][w] + Ic[h][w-1] - Ic[h-1][w-1] + (iceland[h][w] == 'I');
        }
    }

    for (int k = 0; k < K; ++k) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int j = Ja[c][d] - Ja[c][b-1] - Ja[a-1][d] + Ja[a-1][b-1];
        int o = Oc[c][d] - Oc[c][b-1] - Oc[a-1][d] + Oc[a-1][b-1];
        int i = Ic[c][d] - Ic[c][b-1] - Ic[a-1][d] + Ic[a-1][b-1];

        cout << j << " " << o << " " << i << '\n';
    }

    return 0;
}
