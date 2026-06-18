N, M = map(int,input().split())
S = [input() for _ in range(N)]

hoge = [0,0]
for s in S:
    n = s.count('0')
    hoge[n%2] += 1

print(hoge[0]*hoge[1])