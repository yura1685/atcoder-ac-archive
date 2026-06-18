from atcoder.fenwicktree import FenwickTree

N, Q = map(int,input().split())
A = list(map(int,input().split()))

ft = FenwickTree(N)
for i in range(N):
    ft.add(i, A[i])

for _ in range(Q):
    t, x, y = map(int,input().split())
    if t == 0:
        ft.add(x, y)
    else:
        print(ft.sum(x,y))