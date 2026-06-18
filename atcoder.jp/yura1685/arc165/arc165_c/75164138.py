from collections import deque

class DSU:
    '''
    Disjoint Set Union for codon, PyPy3
    頂点集合の統合と連結判定を効率的に行います。

    N: 頂点数
    '''
    N: int
    _parent: list[int]
    __slots__ = ('N', '_parent')
    def __init__(self, N: int) -> None:
        self.N = N
        self._parent = [-1] * N
    def leader(self, Vi: int) -> int:
        '頂点Viの現在の代表元を返します。'
        assert 0 <= Vi < self.N
        Pi = Vi
        while self._parent[Pi] >= 0:
            Pi = self._parent[Pi]
        while Pi != Vi:
            self._parent[Vi], Vi = Pi, self._parent[Vi]
        return Pi
    def merge(self, Ui: int, Vi: int) -> int:
        '頂点Uiと頂点Viを結ぶ辺を追加し、連結成分の代表元を返します。'
        assert 0 <= Ui < self.N and 0 <= Vi < self.N
        Pi, Ci = self.leader(Ui), self.leader(Vi)
        if Pi != Ci:
            if self._parent[Pi] > self._parent[Ci]:
                Pi, Ci = Ci, Pi
            self._parent[Pi] += self._parent[Ci]
            self._parent[Ci] = Pi
        return Pi
    def same(self, Ui: int, Vi: int) -> bool:
        '頂点Uiと頂点Viが連結か判定します。'
        assert 0 <= Ui < self.N and 0 <= Vi < self.N
        return self.leader(Ui) == self.leader(Vi)
    def size(self, Vi: int) -> int:
        '頂点Viの属する連結成分のサイズを返します。'
        assert 0 <= Vi < self.N
        return - self._parent[ self.leader(Vi) ]
    def groups(self) -> list[list[int]]:
        '各連結成分の頂点を昇順に並べたリストを、辞書順に並べ替えて返します。'
        buffer: list[int] = [-1] * self.N
        G: list[list[int]] = []
        for now in range(self.N):
            Pi = now
            while self._parent[Pi] >= 0:
                Pi = self._parent[Pi]
            Bi = buffer[Pi]
            if Bi == -1:
                Bi = buffer[Pi] = len(G)
                G.append([-1] * (- self._parent[Pi]))
            G[Bi][-1] += 1
            G[Bi][G[Bi][-1]] = now
            while Pi != now:
                self._parent[now], now = Pi, self._parent[now]
        return G

I = input().split()
N, M = int(I[0]), int(I[1])
g = [[] for _ in range(N)]
for _ in range(M):
    I = input().split()
    A, B, W = int(I[0])-1, int(I[1])-1, int(I[2])
    g[A].append((W, B))
    g[B].append((W, A))
G = [sorted(x) for x in g]

ok, ng = -1, 10 ** 18
while ng - ok > 1:
    mid = (ok + ng) // 2
    group = [-1] * N
    uf = DSU(N)
    flag = True
    for i in range(N):
        if group[i] != -1:
            continue
        group[i] = 0
        dq = deque([i])
        while dq:
            u = dq.popleft()
            for w, v in G[u]:
                if w >= mid:
                    break
                uf.merge(u, v)
                if group[v] == group[u]:
                    flag = False
                    break
                elif group[v] == -1:
                    group[v] = 1 - group[u]
                    dq.append(v)
            if not flag:
                break
        if not flag:
            break
    if not flag:
        ng = mid
    else:
        hoge = True
        for u in range(N):
            cnt = 0
            wsum = 0
            for w, v in G[u]:
                if w >= mid:
                    break
                if cnt < 2:
                    wsum += w 
                    cnt += 1
                else:
                    break
            if cnt == 2 and wsum < mid:
                hoge = False
                break
        if hoge:
            ok = mid
        else:
            ng = mid

print(ok)