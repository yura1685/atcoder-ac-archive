N = int(input())
A = [int(input()) for _ in range(N)]
B = list(set(A)); B.sort()

d = {}
for i in range(len(B)):
    d[B[i]] = i

for a in A:
    print(d[a])