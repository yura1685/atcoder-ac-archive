from collections import defaultdict

N = int(input())
X = list(map(int,input().split()))

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = 1

while X:
    d = defaultdict(int)
    for x in X:
        for p in prime:
            if x % p == 0:
                d[p] += 1
    hoge = sorted([(d[p],-p) for p in d],reverse=True)
    cnt, maxp = hoge[0]
    ans *= -maxp
    X = [x for x in X if x % maxp != 0]

print(ans)