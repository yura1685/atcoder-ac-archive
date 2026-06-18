n = int(input())
ans = 10**10

for d in range(1,int(n**(0.5)+1)):
    m, r = n // d, n % d
    ans = min(ans, abs(m-d)+r)

print(ans)