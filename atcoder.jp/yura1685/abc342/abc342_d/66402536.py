N = int(input())
A = list(map(int,input().split()))

ans = 0
c = [0]*200010

for x in A:
    y, i = x, 2
    while i*i <= y:
        while y % (i*i) == 0:
            y //= i*i
        i += 1
    ans += c[y]
    c[y] += 1

print(ans + c[0]*(N-c[0]))