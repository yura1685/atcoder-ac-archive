from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
B = [[0]] + [list(map(int,input().split())) for _ in range(N)]

s = set([1])

def dfs(u):
    for i in range(1,B[u][0]+1):
        v = B[u][i]
        if v not in s:
            s.add(v)
            dfs(v)
            print(v,end=' ')

dfs(1)