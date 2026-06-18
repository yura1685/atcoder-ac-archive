N, M, X = map(int,input().split())

book = [list(map(int,input().split())) for _ in range(N)]

ans = 10**10
for bit in range(1 << N):
    money = 0
    skill = [0]*M
    for i in range(N):  # どこにbitが立ってるかを確認していく
        if bit & (1 << i):  # 下からi番目にbitが立っているとき
            money += book[i][0]
            for j in range(1,M+1):
                skill[j-1] += book[i][j]
    if min(skill) >= X:
        ans = min(ans, money)

if ans == 10**10:
    print(-1)
else:
    print(ans)