from more_itertools import run_length

N = int(input())
A = list(map(int,input().split()))

s = list(run_length.encode(A))

ans = 0
for i in s:
    n, c = i
    ans += c // 2

print(ans)