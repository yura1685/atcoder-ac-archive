def level(n):
    if n == 0:
        return ['#']
    ans = []
    c = level(n-1)
    for i in range(1,3**n+1):
        x = c[(i-1)%(3**(n-1))]
        if 3**(n-1)+1 <= i <= 2*3**(n-1):
            ans.append( x + '.'*(3**(n-1)) + x )
        else:
            ans.append(x*3)
    return ans

N = int(input())

hoge = level(N)
for i in hoge:
    print(''.join(i))