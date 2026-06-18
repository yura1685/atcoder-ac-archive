N = int(input())
A = list(map(int,input().split()))
ans = -sum(A)

for bit in range(30):
    x = 0
    cnt = [1, 0]
    for a in A:
        x ^= (a >> bit) & 1
        cnt[x] += 1
    ans += cnt[0] * cnt[1] << bit

print(ans)