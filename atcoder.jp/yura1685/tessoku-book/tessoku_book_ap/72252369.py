N, K = map(int,input().split())
P = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0
for a in range(1,101):
    for b in range(1,101):
        cnt = 0
        for A, B in P:
            if a <= A <= a + K and b <= B <= b + K:
                cnt += 1
        ans = max(ans, cnt)

print(ans)