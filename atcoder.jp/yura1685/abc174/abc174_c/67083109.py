K = int(input())

cnt = [0]*K
ans = 0
sev = 0

while True:
    sev = (sev*10 + 7) % K
    ans += 1
    if sev == 0:
        print(ans)
        exit()
    if cnt[sev] == 1:
        print(-1)
        exit()
    cnt[sev] += 1
