N = int(input())
A = list(map(int,input().split()))

s = sum(A)
c = [0]*100001

for a in A:
    c[a] += 1

Q = int(input())
for _ in range(Q):
    B, C = map(int,input().split())
    s += (C-B)*c[B]
    c[C] += c[B]
    c[B] = 0
    print(s)