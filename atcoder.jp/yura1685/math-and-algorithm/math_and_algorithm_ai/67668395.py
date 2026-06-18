N, Q = map(int,input().split())
A = list(map(int,input().split()))
guest = [0]*(N+1)
man = 0
for i in range(N):
    man += A[i]
    guest[i+1] = man

for _ in range(Q):
    l, r = map(int,input().split())
    print(guest[r]-guest[l-1])