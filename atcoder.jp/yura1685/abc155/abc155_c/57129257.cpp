#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

int main() {
    int N;
    std::cin >> N;

    // アイテムのカウント用マップ
    std::map<std::string, int> counter;

    // 入力を読み取ってカウント
    for (int i = 0; i < N; ++i) {
        std::string item;
        std::cin >> item;
        ++counter[item];
    }

    // 最大カウント数を取得
    int max_count = 0;
    for (const auto& pair : counter) {
        if (pair.second > max_count) {
            max_count = pair.second;
        }
    }

    // 最大カウントを持つアイテムのリストを作成
    std::vector<std::string> most_common_items;
    for (const auto& pair : counter) {
        if (pair.second == max_count) {
            most_common_items.push_back(pair.first);
        }
    }

    // アイテムをソート
    std::sort(most_common_items.begin(), most_common_items.end());

    // 出力
    for (const auto& item : most_common_items) {
        std::cout << item << std::endl;
    }

    return 0;
}
