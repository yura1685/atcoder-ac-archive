def swap(s:str, left:int, right:int):
    x = list(s)
    xl, xr, y = x[:left-1], x[right:], x[left-1:right]
    y = list(reversed(y))
    ans = xl + y + xr
    return ''.join(ans)

S = input()
N = int(input())
for _ in range(N):
    l, r = map(int,input().split())
    S = swap(S, l, r)
print(S)