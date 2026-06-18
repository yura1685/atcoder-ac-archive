N = int(input())
A = list(map(int,input().split()))
B = list(set(A))
B.sort()
d = {}
for i in range(len(B)):
    d[B[i]] = i+1

for a in A:
    print(d[a],end=' ')