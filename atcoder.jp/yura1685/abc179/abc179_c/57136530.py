N = int(input())
ans = 0
for a in range(1,N):
    for b in range(1,N):
        c = N - a*b
        if c > 0:
            ans += 1
        else:
            break
print(ans)