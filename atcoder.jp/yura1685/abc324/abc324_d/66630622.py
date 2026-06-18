N = int(input())
S = list(input())
S.sort()

ans = 0
for n in range(10**7):
    sq = str(n*n)
    if len(sq) > N:
        break
    sq += '0'*(N-len(sq))
    sq = sorted(list(sq))
    if S == sq:
        ans += 1
print(ans)