from sys import setrecursionlimit as srl
srl(10**8)
N = int(input())
A = [list(map(int,input().split())) for _ in range(2*N-1)]
ans = 0

def dfs(lst, s):
    if len(lst) == N:
        global ans
        res = 0
        for i, j in lst:
            res ^= A[i][j-i-1]
        ans = max(ans,res)
        return 
    for i in range(2*N):
        if i not in s:
            nex = i
            break
    for j in range(nex+1,2*N):
        if j not in s:
            dfs(lst+[(i,j)], s|{i,j})

dfs([],set())

print(ans)