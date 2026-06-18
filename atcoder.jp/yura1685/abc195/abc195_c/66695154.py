N = int(input())

ans = 0
for n in range(1,7):
    ans += max(0, N-1000**n+1)

print(ans)