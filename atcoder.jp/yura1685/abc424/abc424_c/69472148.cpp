// Original Python Code
// from sys import setrecursionlimit
// setrecursionlimit(10**8)

// N = int(input())
// g = [[] for _ in range(N+1)]
// c = [0] * (N+1)
// s = set()
// for i in range(1,N+1):
//     A, B = map(int,input().split())
//     if A == B == 0:
//         c[i] = 1
//         s.add(i)
//     else:
//         g[A].append(i)
//         g[B].append(i)

// def dfs(u):
//     for v in g[u]:
//         if c[v] == 0:
//             c[v] = 1
//             dfs(v)

// for u in s:
//     dfs(u)

// print(sum(c))

#include <iostream>
#include <vector>
#include <numeric>
#include <set>

std::vector<std::vector<int>> g;
std::vector<int> c;
std::set<int> s;

void dfs(int u) {
    for (int v : g[u]) {
        if (c[v] == 0) {
            c[v] = 1;
            dfs(v);
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N;

    g.resize(N + 1);
    c.resize(N + 1, 0);

    for (int i = 1; i <= N; ++i) {
        int A, B;
        std::cin >> A >> B;
        if (A == 0 && B == 0) {
            c[i] = 1;
            s.insert(i);
        } else {
            g[A].push_back(i);
            g[B].push_back(i);
        }
    }

    for (int u : s) {
        dfs(u);
    }

    int sum_c = 0;
    for (int val : c) {
        sum_c += val;
    }

    std::cout << sum_c << std::endl;

    return 0;
}