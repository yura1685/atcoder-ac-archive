X = int(input())
N = 4*X - 1

ans = []
p = 1
while p*p <= abs(N):
    if N % p == 0:
        if (N//p - p - 2) % 4 == 0:
            ans.append((N//p - p - 2)//4)
        if (N//(-p) + p - 2) % 4 == 0:
            ans.append((N//(-p) + p - 2)//4)
    p += 2

ans.sort()
print(len(ans))
print(*ans)