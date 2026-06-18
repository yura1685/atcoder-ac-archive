// Original Python code:
// n = int(input())
// ans = 0
//
// def is_prime(n):
//     if n == 1:
//         return False
//     root = int(n**(0.5))
//     for i in range(2,root+1):
//         if n % i == 0:
//             return False
//     return True
//
// for i in range(1,n):
//     ans += is_prime(i)
//
// print(ans)

#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n == 1) return false;
    int root = static_cast<int>(sqrt(n));
    for (int i = 2; i <= root; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 1; i < n; ++i) {
        ans += is_prime(i);
    }
    cout << ans << endl;
    return 0;
}
