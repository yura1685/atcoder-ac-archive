N = int(input())
c = []
for i in range(N):
    c = c + [i+1] + c
print(*c)