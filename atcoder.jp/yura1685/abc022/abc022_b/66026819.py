N = int(input())
flo = [0]*(10**5+1)

jufun = 0

for _ in range(N):
    a = int(input())
    if flo[a] == 1:
        jufun += 1
    else:
        flo[a] += 1

print(jufun)