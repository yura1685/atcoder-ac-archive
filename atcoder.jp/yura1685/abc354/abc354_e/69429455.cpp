#include <iostream>
#include <vector>
#include <map>
#include <tuple>

using namespace std;

// 構造体を定義して、タプルのハッシュを有効にする
struct VectorHasher {
    long long operator()(const vector<int>& v) const {
        long long hash_val = 0;
        for (int i : v) {
            hash_val = hash_val * 31 + i; // 単純なハッシュ関数
        }
        return hash_val;
    }
};

map<vector<int>, int> memo;
vector<pair<int, int>> pair_list;
vector<pair<int, int>> card_list;

int dfs(vector<int> c, int t) {
    if (memo.count(c)) {
        return memo[c];
    }

    bool can_win = false;
    for (const auto& p : pair_list) {
        int i = p.first;
        int j = p.second;
        
        vector<int> next_c = c;
        bool valid_move = false;

        if (i == j && c[i] >= 2) {
            next_c[i] -= 2;
            valid_move = true;
        } else if (i != j && c[i] >= 1 && c[j] >= 1) {
            next_c[i] -= 1;
            next_c[j] -= 1;
            valid_move = true;
        }

        if (valid_move) {
            if (dfs(next_c, t ^ 1) == t) {
                can_win = true;
                break;
            }
        }
    }

    if (can_win) {
        memo[c] = t;
        return t;
    } else {
        memo[c] = t ^ 1;
        return t ^ 1;
    }
}

int main() {
    int N;
    cin >> N;

    map<pair<int, int>, int> card_map;

    for (int i = 0; i < N; ++i) {
        int a, b;
        cin >> a >> b;
        card_map[{a, b}]++;
    }

    vector<int> tup_list;
    for (const auto& entry : card_map) {
        card_list.push_back(entry.first);
        tup_list.push_back(entry.second);
    }
    
    int num_unique_cards = card_list.size();
    for (int i = 0; i < num_unique_cards; ++i) {
        for (int j = i; j < num_unique_cards; ++j) {
            if (card_list[i].first == card_list[j].first || card_list[i].second == card_list[j].second) {
                pair_list.push_back({i, j});
            }
        }
    }

    int result = dfs(tup_list, 1);
    
    if (result == 1) {
        cout << "Takahashi" << endl;
    } else {
        cout << "Aoki" << endl;
    }

    return 0;
}