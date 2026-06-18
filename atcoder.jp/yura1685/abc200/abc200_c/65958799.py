N = int(input())
A = list(map(int,input().split()))

d = [0]*201

for a in A:
    d[a % 200] += 1

ans = 0
for i in d:
    ans += i*(i-1)

print(ans//2)