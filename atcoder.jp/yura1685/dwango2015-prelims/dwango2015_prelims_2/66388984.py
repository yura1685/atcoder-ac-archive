from more_itertools import run_length

S = input()
S = S.replace('25','X')

c = run_length.encode(S)
def f(n):
    return n*(n+1)//2

ans = 0
for x, y in c:
    if x == 'X':
        ans += f(y)

print(ans)