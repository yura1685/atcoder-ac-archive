S = input()
ans = 1685
for alp in 'qwertyuiopasdfghjklzxcvbnm':
    N = len(S)
    t = [1 if s == alp else 0 for s in S]
    if sum(t) == 0: continue
    cnt = 0
    while True:
        if sum(t) == N - cnt: ans = min(ans, cnt); break
        t = [max(t[i], t[i+1]) for i in range(len(t)-1)]
        cnt += 1
print(ans)