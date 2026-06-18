N = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True)

ans = 10**4
A, B, C = coin

for a in range(10000):
    if A*a > N:
        break
    for b in range(10000-a):
        if A*a + B*b > N:
            break
        if (N-A*a-B*b) % C == 0:
            c = (N-A*a-B*b) // C
            ans = min(ans,a+b+c)

print(ans)