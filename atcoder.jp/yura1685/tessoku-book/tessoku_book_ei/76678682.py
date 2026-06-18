from sys import exit

I = input().split()
N, M = int(I[0]), int(I[1])
g:list[list[int]] = [[] for _ in range(N)]
for _ in range(M):
    I = input().split()
    A, B = int(I[0]), int(I[1])
    g[A-1].append(B-1)
    g[B-1].append(A-1)

path:list[int] = [0]
In:list[bool] = [False] * N
In[0] = True

def dfs(u: int):
    for v in g[u]:
        if v == N-1:
            path.append(v)
            ans = [n + 1 for n in path]
            for a in ans:
                print(a)
            exit(0)
        if In[v] == True:
            pass
        else:
            In[v] = True
            path.append(v)
            dfs(v)
            path.pop()
            In[v] = False
    
dfs(0)