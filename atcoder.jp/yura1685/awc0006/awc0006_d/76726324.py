N, M = map(int, input().split())
LR = sorted([tuple(map(int, input().split())) for _ in range(M)], reverse=True)
now = 1
ans = 0
while LR:
    L, R = LR.pop()
    if now < L:
        exit(print(-1))
    elif R < now:
        pass
    else:
        nxt = max(now - 1, R)
        while LR:
            next_L, next_R = LR.pop()
            if next_L <= now:
                nxt = max(nxt, next_R)
            else:
                LR.append((next_L, next_R))
                break
                
        ans += 1
        now = nxt + 1

print(ans if now > N else -1)