import sys
sys.setrecursionlimit(10**9)

d = {1:0} #数字が大きいとあれだからちっちゃい順に整列
b = {0:1} #上記の逆。dの反対はb←好き
cnt = 1 #dにいれる数字。既に0は入ってるので1から
g = [[] for _ in range(400010)]

N = int(input())
for _ in range(N):
    A, B = map(int,input().split())
    if d.get(A) == None: #辞書に登録
        d[A] = cnt
        b[cnt] = A
        cnt += 1
    if d.get(B) == None:
        d[B] = cnt
        b[cnt] = B
        cnt += 1
    g[d[A]].append(d[B])
    g[d[B]].append(d[A])

check = [0]*400010
check[0] = 1 #頂点0からスタートするので探索済みにする
ans = [1]
def dfs(u):
    for v in g[u]: #uに接続する頂点vについて調べる。
        if check[v] == 0:
            check[v] = 1
            ans.append(b[v])
            dfs(v)

dfs(0)
print(max(ans))