from collections import defaultdict
from bisect import bisect_left as b_l, bisect_right as b_r

N = int(input())
A = list(map(int, input().split()))

mods = [1685168516851685029, 1685168516851685057, 1685168516851685059]

M = max(A) + 20

L = [0] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] <= A[i]:
        stack.pop()
    if stack:
        L[i] = stack[-1] + 1
    stack.append(i)

R = [N-1] * N
stack = []
for i in range(N-1, -1, -1):
    while stack and A[stack[-1]] < A[i]:
        stack.pop()
    if stack:
        R[i] = stack[-1] - 1
    stack.append(i)

def solve(mod):
    pow2 = [1] * (M + 1)
    for i in range(M):
        pow2[i+1] = pow2[i] * 2 % mod

    pow2_ac = [0] * (N+1)
    for i in range(N):
        pow2_ac[i+1] = (pow2_ac[i] + pow2[A[i]]) % mod

    pos = defaultdict(list)
    for i in range(N+1):
        pos[pow2_ac[i]].append(i)

    ans = 0
    for i in range(N):
        left = i - L[i] + 1
        right = R[i] - i + 1
        for k in range(A[i], min(A[i] + 20, M + 1)):
            pk = pow2[k]
            if left <= right:
                for l in range(L[i], i+1):
                    target = (pow2_ac[l-1] + pk) % mod
                    if target in pos:
                        lst = pos[target]
                        ans += b_r(lst, R[i]+1) - b_l(lst, i+1)
            else:
                for r in range(i+1, R[i]+2):
                    target = (pow2_ac[r] - pk) % mod
                    if target in pos:
                        lst = pos[target]
                        ans += b_r(lst, i-1) - b_l(lst, L[i]-1)
    return ans

anss = [solve(mod) for mod in mods]
print(sum(anss) - max(anss) - min(anss) + N)