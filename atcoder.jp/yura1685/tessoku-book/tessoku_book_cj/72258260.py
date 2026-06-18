from bisect import bisect_left
N = int(input())
A = sorted(map(int,input().split()))
Q = int(input())
for _ in range(Q):
    x = int(input())
    print(bisect_left(A, x))