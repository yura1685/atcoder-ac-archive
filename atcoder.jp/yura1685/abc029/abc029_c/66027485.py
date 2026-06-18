import itertools

n = int(input())
a = ['a','b','c']

def bit3(n):
    return list(itertools.product([0,1,2], repeat=n))

c = bit3(n)
for x in c:
    hoge = ''
    for i in range(n):
        hoge += a[x[i]]
    print(hoge)