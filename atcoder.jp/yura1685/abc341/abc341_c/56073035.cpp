#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int H, W, N;
    cin >> H >> W >> N;
    string route;
    cin >> route;

    vector<string> Land(H);
    for (int i = 0; i < H; ++i) {
        cin >> Land[i];
    }

    int pattern = 0;

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            int Si = i, Sj = j;
            if (Land[i][j] == '.') {
                bool valid = true;
                for (int k = 0; k < N; ++k) {
                    if (route[k] == 'L') {
                        if (Sj > 0 && Land[Si][Sj - 1] == '.') {
                            --Sj;
                        } else {
                            valid = false;
                            break;
                        }
                    } else if (route[k] == 'R') {
                        if (Sj < W - 1 && Land[Si][Sj + 1] == '.') {
                            ++Sj;
                        } else {
                            valid = false;
                            break;
                        }
                    } else if (route[k] == 'U') {
                        if (Si > 0 && Land[Si - 1][Sj] == '.') {
                            --Si;
                        } else {
                            valid = false;
                            break;
                        }
                    } else if (route[k] == 'D') {
                        if (Si < H - 1 && Land[Si + 1][Sj] == '.') {
                            ++Si;
                        } else {
                            valid = false;
                            break;
                        }
                    }
                }
                if (valid && Land[Si][Sj] == '.') {
                    ++pattern;
                }
            }
        }
    }

    cout << pattern << endl;

    return 0;
}
