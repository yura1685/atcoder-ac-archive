from collections import defaultdict

N, M = map(int, input().split())
X = list(map(int, input().split()))
D = [defaultdict(int) for _ in range(M)]
for x in X: D[x % M][x] += 1

ans = sum(D[0].values()) // 2
if M % 2 == 0: ans += sum(D[M//2].values()) // 2

for i in range(1, (M + 1) // 2):
    A, B = D[i], D[M-i]
    if sum(A.values()) > sum(B.values()):
        A, B = B, A
    S_A = sum(A.values())
    S_B = sum(B.values())
    oddB = sum(b % 2 for b in B.values())
    if S_A <= oddB:
        ans += S_A  + sum(b // 2 for b in B.values())
    else:
        ans += (S_A + S_B) // 2

print(ans)