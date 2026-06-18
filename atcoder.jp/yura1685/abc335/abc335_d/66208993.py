N = int(input())

def f(n):
    if n == 3:
        return [[1,2,3],[8,'T',4],[7,6,5]]
    else:
        c = f(n-2)
    for h in range(n-2):
        for w in range(n-2):
            if c[h][w] == 'T': # type: ignore
                continue
            c[h][w] += 4*(n-1)
    for i in range(n-2):
        c[i] = [4*(n-1)-i] + c[i] + [n+i+1]
    c = [[i for i in range(1,n+1)]] + c + [[3*(n-1)+1-i for i in range(n)]]
    return c

for i in f(N):
    print(*i)