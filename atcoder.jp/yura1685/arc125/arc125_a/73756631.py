N, M = map(int, input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

cost = 16851685
for i in range(1, N):
    if S[0] != S[i]:
        cost = min(cost, min(i, N-i))

now = S[0]
ans = 0
for t in T:
    if now != t:
        now = 1 - now
        ans += cost
        cost = 1
    ans += 1

print(ans if ans < 16851685 else -1)