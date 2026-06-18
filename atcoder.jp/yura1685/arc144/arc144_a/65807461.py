N = int(input())

def f(n: int):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans

M = 2*N
yura = N // 4
ra = N - 4*yura
if ra == 0:
    ra = ''
print(M)
print(str(ra) + '4'*yura)