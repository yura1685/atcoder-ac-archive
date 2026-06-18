def f(n):
    c = 0
    for i in str(n):
        c += int(i)
    return c

N = int(input())
ans = []
for x in range(max(0,N-200),N+1):
    if x + f(x) == N:
        ans .append(x)

print(len(ans))
for i in ans: print(i)