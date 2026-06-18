from collections import defaultdict

H, W = map(int, input().split())
N = int(input())
D = defaultdict(int)
for _ in range(N):
    A, B = map(int, input().split())
    D[(A, B)] += 1

ans = 0
for a, b in D:
    for i in range(3):
        for j in range(3):
            cnt = 0
            for h in range(a - i, a - i + 3):
                for w in range(b - j, b - j + 3):
                    if (h, w) in D:
                        cnt += D[(h, w)]
            ans = max(ans, cnt)

print(ans)