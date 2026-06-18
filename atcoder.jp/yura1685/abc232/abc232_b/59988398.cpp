#include <iostream>
#include <string>
using namespace std;

int main() {
    string S, T;
    cin >> S >> T;

    // アルファベットの総数
    const int ALPHABET_COUNT = 26;

    // 0から25の全シフト量を試す
    for (int i = 0; i < ALPHABET_COUNT; ++i) {
        string cipher = "";

        // Sを1文字ずつ処理
        for (char c : S) {
            // シフト後の文字を計算（範囲を循環するために 'a' を基準にする）
            char shifted = 'a' + (c - 'a' + i) % ALPHABET_COUNT;
            cipher += shifted;
        }

        // シフト結果がTと一致するか
        if (cipher == T) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    // どのシフト量でも一致しなかった場合
    cout << "No" << endl;
    return 0;
}
