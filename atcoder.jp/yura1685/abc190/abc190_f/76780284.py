from atcoder.fenwicktree import FenwickTree

N = int(input())
A = list(map(int, input().split()))
ft = FenwickTree(N)
inv = 0
for a in A:
    ft.add(a, 1)
    inv += ft.sum(a + 1, N)
print(inv)
for i in range(N-1):
    a = A[i]
    inv = inv - a + (N - a - 1)
    print(inv)