N, Q = map(int,input().split())
S = input()

AC = [0]*(N+1)

ac = 0
for i in range(1,N):
    if S[i-1] == 'A' and S[i] == 'C':
        ac += 1
    AC[i+1] = ac

for _ in range(Q):
    l, r = map(int,input().split())
    print(AC[r]-AC[l])