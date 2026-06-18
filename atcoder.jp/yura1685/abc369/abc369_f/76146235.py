from atcoder.segtree import SegTree

H, W, N = map(int, input().split())
s = SegTree(max, (0, -1), [(0, -1) for w in range(W)])

C = []
for i in range(N):
    h, w = map(int, input().split())
    C.append((h, w, i))
C.sort()

prev = [-1] * N
dp = [0] * N

for h, w, i in C:
    h, w = h-1, w-1
    M, pi = s.prod(0, w+1)
    prev[i] = pi
    dp[i] = M + 1
    s.set(w, (M+1, i))

M, now = s.all_prod()

path = []
while now != -1:
    path.append(now)
    now = prev[now]

hw = {}
for h, w, i in C:
    hw[i] = (h, w)

P = [(1, 1)]
for i in path[::-1]:
    P.append(hw[i])
P.append((H, W))

ans = []
for i in range(len(P) - 1):
    h1, w1 = P[i]
    h2, w2 = P[i+1]
    ans.append('D' * (h2 - h1))
    ans.append('R' * (w2 - w1))

print(M)
print(''.join(ans))