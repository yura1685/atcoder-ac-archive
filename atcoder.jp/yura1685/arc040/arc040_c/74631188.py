N = int(input())
S = [list(input()) for _ in range(N)]
ans = 0

for h in range(N):
    for w in reversed(range(N)):
        if S[h][w] == '.':
            ans += 1
            for x in range(w+1):
                S[h][x] = 'o'
            if h + 1 < N:
                for x in range(w,N):
                    S[h+1][x] = 'o'

print(ans)