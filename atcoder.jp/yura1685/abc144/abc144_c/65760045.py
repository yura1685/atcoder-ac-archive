def distance(P):
    return P[0] + P[1] - 2

N = int(input())
ans = 10**12
for d in range(1,int(N**(0.5))+1):
    if N % d == 0:
        ans = min(ans, distance([d,N//d]))

print(ans)