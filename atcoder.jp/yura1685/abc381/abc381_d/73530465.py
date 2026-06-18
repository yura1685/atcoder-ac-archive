from more_itertools import run_length

N = int(input())
A = list(map(int,input().split()))
B = []
for n, cnt in run_length.encode(A):
    if cnt == 1:
        if (B and B[-1] < 0) or not B:
            pass
        else:
            B.append(-1)
    if cnt == 2:
        B.append(n)
    if cnt > 2:
        B.append(n); B.append(-1); B.append(n)

if B and B[-1] == -1: B.pop()

M = len(B)
cnt = [0] * (N+1)
now = 0
l = 0
ans = 0

for r in range(M):
    if B[r] == -1:
        while l < r:
            cnt[B[l]] = 0
            l += 1
        l = r + 1
        now = 0
        continue

    elif cnt[B[r]] == 1:
        while True:
            if B[l] == B[r]:
                l += 1
                break
            cnt[B[l]] = 0
            l += 1
            now -= 1

    else:
        cnt[B[r]] = 1
        now += 1
        
    ans = max(ans, now)

print(2*ans)