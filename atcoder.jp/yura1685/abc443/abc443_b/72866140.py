N, K = map(int,input().split())
i = N
x = 0
while x < K:
    x += i
    i += 1

print(i-N-1)