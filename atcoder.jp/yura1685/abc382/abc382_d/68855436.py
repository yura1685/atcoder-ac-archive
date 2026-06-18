N, M = map(int,input().split())

def dfs(n,m): # n項・末尾がm以下の全て
    if n == 1:
        return [[i] for i in range(1,11)]
    res = []
    for lst in dfs(n-1,m-10):
        x = lst[-1]
        for i in range(x+10,m+1):
            res.append(lst+[i])
    return res

ans = sorted(dfs(N,M))

print(len(ans))
for L in ans:
    print(*L)