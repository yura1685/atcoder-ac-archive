from typing import List, Tuple

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
N, X, Y = int(I[0]), int(I[1]), int(I[2])
P:List[Tuple[int, int, int, int]] = [(0,0,X-1,Y-1)]
for _ in range(N):
    nex_P = []
    Q = input().split()
    A, B = int(Q[1]), int(Q[2])
    if Q[0] == 'X':
        for lx, ly, rx, ry in P:
            if rx < A:
                nex_P.append((lx, ly-B, rx, ry-B))
            elif A <= lx:
                nex_P.append((lx, ly+B, rx, ry+B))
            else:
                nex_P.append((lx, ly-B, A-1, ry-B))
                nex_P.append((A, ly+B, rx, ry+B))
    else:
        for lx, ly, rx, ry in P:
            if ry < A:
                nex_P.append((lx-B, ly, rx-B, ry))
            elif A <= ly:
                nex_P.append((lx+B, ly, rx+B, ry))
            else:
                nex_P.append((lx-B, ly, rx-B, A-1))
                nex_P.append((lx+B, A, rx+B, ry))
    P = nex_P.copy()

Size = len(P)
uf = DSU(Size)

for i in range(Size-1):
    for j in range(i+1, Size):
        lxi, lyi, rxi, ryi = P[i]
        lxj, lyj, rxj, ryj = P[j]
        if (rxi+1 == lxj or rxj+1 == lxi) and max(lyi,lyj) <= min(ryi,ryj):
            uf.merge(i,j)
        elif (ryi+1 == lyj or ryj+1 == lyi) and max(lxi,lxj) <= min(rxi,rxj):
            uf.merge(i,j)

ans = []
for g in uf.groups():
    s = 0
    for u in g:
        lx, ly, rx, ry = P[u]
        s += (rx-lx+1) * (ry-ly+1)
    ans.append(s)

ans.sort()
print(len(ans))
for a in ans:
  print(a, end=' ')