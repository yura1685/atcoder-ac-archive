R, G, B, N = map(int,input().split())

ans = 0
for r in range(N+1):
    if R*r > N:
        break
    for g in range(N+1):
        if R*r + G*g > N:
            break
        ball = N-R*r-G*g
        if ball % B == 0:
            ans += 1

print(ans)