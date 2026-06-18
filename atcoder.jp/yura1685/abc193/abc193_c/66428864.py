N = int(input())
root = int(N**(1/2))

s = set()

for i in range(2,root+1):
    n = i*i
    while n <= N:
        s.add(n)
        n *= i

print(N-len(s))