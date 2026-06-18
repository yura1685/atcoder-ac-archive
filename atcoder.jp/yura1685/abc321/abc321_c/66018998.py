from itertools import combinations

def kumi():
    L = [i for i in range(10)]
    ans = []
    for i in range(1,11):
        for x in combinations(L, i):
            y = list(x)
            y.sort(reverse=True)
            hoge = ''
            for i in y:
                hoge += str(i)
            ans.append(int(hoge))
    ans.sort()
    return ans

K = int(input())
print(kumi()[K])