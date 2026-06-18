N:int = int(input())
A:list[int] = list(map(int, input().split()))
ans = set()

def f(T:list[int]) -> None:
    X:list[int] = [0] * N
    for i in range(N):
        X[T[i] - 1] += A[i]
    xor = 0
    for x in X:
        xor ^= x 
    ans.add(xor)

def dfs(L:list[int], M:int) -> None:
    if len(L) == N:
        f(L)
    else:
        for g in range(1,M+1):
            L.append(g)
            dfs(L, M)
            L.pop()
        
        L.append(M+1)
        dfs(L, M+1)
        L.pop()

dfs([1], 1)

print(len(ans))