#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;

    // 'C'で区切って'A'と'B'の部分を抽出
    vector<string> c;
    string temp = "";
    for (char ch : S) {
        if (ch == 'C') {
            if (!temp.empty()) {
                c.push_back(temp);
                temp.clear();
            }
        } else {
            temp += ch;
        }
    }
    if (!temp.empty()) c.push_back(temp);

    // 'A'と'B'の変換処理
    vector<string> d;
    for (const string &i : c) {
        int a = 0, b = 0;
        for (char ch : i) {
            if (ch == 'A') a++;
            if (ch == 'B') b++;
        }
        string result = string(a + b / 2, 'A') + string(b % 2, 'B');
        d.push_back(result);
    }

    // 出力用の文字列Xを構築
    string X = "";
    size_t d_index = 0;
    size_t s_index = 0;

    while (s_index < S.size()) {
        if (S[s_index] == 'C') {
            X += 'C';
            s_index++;
        } else {
            X += d[d_index];
            d_index++;
            while (s_index < S.size() && S[s_index] != 'C') {
                s_index++;
            }
        }
    }

    cout << X << endl;

    return 0;
}
