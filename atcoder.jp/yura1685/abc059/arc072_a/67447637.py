n = int(input())
A = list(map(int,input().split()))
B = [-a for a in A]

def solve(g):
    ans = 0
    s = 0
    for i in range(n): # i % 2 == 0 なら正に，i % 2 == 1 なら負に調整
        s += g[i]
        if i % 2 == 0:
            if s > 0:
                continue
            ans += - s + 1
            s = 1
        if i % 2 == 1:
            if s < 0:
                continue
            ans += s + 1
            s = -1
    return ans

print(min(solve(A),solve(B)))