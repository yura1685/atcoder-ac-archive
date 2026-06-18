H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for h1 in range(H):
    for h2 in range(h1, H):
        for w1 in range(W):
            for w2 in range(w1, W):
                flag = False
                for h in range(h2-h1+1):
                    for w in range(w2-w1+1):
                        if S[h+h1][w+w1] != S[h2-h][w2-w]:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    ans += 1

print(ans)