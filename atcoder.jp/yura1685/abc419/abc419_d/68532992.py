N, M = map(int,input().split())
S = input()
T = input()
swap = [0]*(N+1)
# swap[i] = 1 のとき，swapしてから読む
for _ in range(M):
    L, R = map(int,input().split())
    swap[L-1] ^= 1
    swap[R] ^= 1

ans = []

now = 1
for i in range(N):
    if swap[i]:
        now ^= 1
    if now:
        ans.append(S[i])
    else:
        ans.append(T[i])

print(''.join(ans))