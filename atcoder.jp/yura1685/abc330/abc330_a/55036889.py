N, L = map(int, input(). split())
Li = list(map(int, input(). split()))
ans = 0
for i in range(N):
    if Li[i] >= L:
        ans += 1
print(ans)