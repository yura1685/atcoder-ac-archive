// from collections import deque
// 
// N, Q = map(int,input().split())
// 
// dragon = deque((i,0) for i in range(1,N+1))
// 
// for _ in range(Q):
//     n, q = map(str,input().split())
//     if n == '1':
//         head_x, head_y = dragon[0]
//         if q == 'U':
//             head_y += 1
//         elif q == 'D':
//             head_y -= 1
//         elif q == 'R':
//             head_x += 1
//         elif q == 'L':
//             head_x -= 1
//         dragon.appendleft((head_x, head_y))
//         dragon.pop()
//     elif n == '2':
//         q = int(q)
//         print(*dragon[q-1])

#include <iostream>
#include <deque>
#include <string>
#include <utility>

using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    deque<pair<int, int>> dragon;
    for (int i = 1; i <= N; ++i) {
        dragon.push_back({i, 0});
    }

    for (int i = 0; i < Q; ++i) {
        string n, q;
        cin >> n >> q;

        if (n == "1") {
            int head_x = dragon.front().first;
            int head_y = dragon.front().second;

            if (q == "U") {
                head_y += 1;
            } else if (q == "D") {
                head_y -= 1;
            } else if (q == "R") {
                head_x += 1;
            } else if (q == "L") {
                head_x -= 1;
            }

            dragon.push_front({head_x, head_y});
            dragon.pop_back();
        } else if (n == "2") {
            int idx = stoi(q);
            cout << dragon[idx - 1].first << " " << dragon[idx - 1].second << endl;
        }
    }

    return 0;
}
