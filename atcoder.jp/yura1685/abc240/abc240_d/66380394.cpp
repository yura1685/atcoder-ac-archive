// Original Python code:
// N = int(input())
// A = list(map(int,input().split()))
//
// tutu  = []
// color = []
// count = []
//
// for i in range(N):
//     a = A[i]
//     if not tutu:
//         tutu.append(a)
//         color.append(a)
//         count.append(1)
//         print(1)
//     else:
//         if color[-1] == a:
//             if count[-1] + 1 == a:
//                 color.pop()
//                 count.pop()
//                 tutu = tutu[:-a+1]
//                 print(len(tutu))
//             else:
//                 tutu.append(a)
//                 count[-1] += 1
//                 print(len(tutu))
//         else:
//             tutu.append(a)
//             color.append(a)
//             count.append(1)
//             print(len(tutu))

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<int> tutu;
    vector<int> color;
    vector<int> count;

    for (int i = 0; i < N; ++i) {
        int a = A[i];
        if (tutu.empty()) {
            tutu.push_back(a);
            color.push_back(a);
            count.push_back(1);
            cout << 1 << endl;
        } else {
            if (color.back() == a) {
                if (count.back() + 1 == a) {
                    color.pop_back();
                    count.pop_back();
                    tutu.resize(tutu.size() - a + 1);
                    cout << tutu.size() << endl;
                } else {
                    tutu.push_back(a);
                    count.back() += 1;
                    cout << tutu.size() << endl;
                }
            } else {
                tutu.push_back(a);
                color.push_back(a);
                count.push_back(1);
                cout << tutu.size() << endl;
            }
        }
    }

    return 0;
}
