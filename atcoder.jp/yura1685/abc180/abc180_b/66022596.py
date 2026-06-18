N = int(input())
x = list(map(int,input().split()))

def man(l):
    d = 0
    for i in l:
        d += abs(i)
    return d

def euc(l):
    d = 0
    for i in l:
        d += i**2
    return d**(0.5)

def che(l):
    d = 0
    for i in l:
        d = max(d,abs(i))
    return d

print(man(x)); print(euc(x)); print(che(x))