from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))
B = [b for b in A[::-1]]

def solve(L):
    d = defaultdict(int)
    res = 0
    for x in L:
        if x % 5: d[x] += 1
        else:
            res += d[x//5*3] * d[x//5*7]
            d[x] += 1
    return res

print(solve(A) + solve(B))