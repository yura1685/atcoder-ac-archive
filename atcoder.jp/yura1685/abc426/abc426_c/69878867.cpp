// 元のPythonコード
// from sortedcontainers import SortedSet
//
// N, Q = map(int,input().split())
// IN = [1] * N
//
// ss = SortedSet((i,1) for i in range(N))
// for _ in range(Q):
//     X, Y = map(int,input().split())
//     X, Y = X-1, Y-1
//     cnt = 0
//     while ss and ss[0][0] <= X:
//         os, c = ss.pop(0)
//         IN[os] = 0
//         cnt += c
//     if IN[Y]:
//         ss.discard((Y,IN[Y]))
//         print(cnt)
//         IN[Y] += cnt
//         ss.add((Y,IN[Y]))
//     else:
//         print(cnt)
//         ss.add((Y,IN[Y]))

#include <iostream>
#include <vector>
#include <set>
#include <utility>

void solve() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N, Q;
    if (!(std::cin >> N >> Q)) return;

    std::vector<int> IN(N, 1);
    std::set<std::pair<int, int>> ss;

    for (int i = 0; i < N; ++i) {
        ss.insert({i, 1});
    }

    for (int _ = 0; _ < Q; ++_) {
        int X_in, Y_in;
        if (!(std::cin >> X_in >> Y_in)) break;
        
        int X = X_in - 1;
        int Y = Y_in - 1;
        
        int cnt = 0;
        
        while (!ss.empty()) {
            auto it = ss.begin();
            
            if (it->first > X) {
                break; 
            }

            int os = it->first;
            int c = it->second;

            ss.erase(it);

            IN[os] = 0;
            cnt += c;
        }

        if (IN[Y] > 0) {
            ss.erase({Y, IN[Y]});

            std::cout << cnt << "\n";
            
            IN[Y] += cnt;

            ss.insert({Y, IN[Y]});
        } 
        else {
            std::cout << cnt << "\n";
            
            ss.insert({Y, IN[Y]});
        }
    }
}

int main() {
    solve();
    return 0;
}