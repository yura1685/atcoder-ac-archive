import typing


class DSU:
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n
        self.top = [[i] for i in range(n)]

    def find(self, x):
            if self.parent_or_size[x] < 0:
                return x
            else:
                self.parent_or_size[x] = self.find(self.parent_or_size[x])
                return self.parent_or_size[x]

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.find(a)
        y = self.find(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        self.top[x] += self.top[y]
        self.top[x] = sorted(self.top[x], reverse=True)[:10]

        return x
    
N, Q = map(int,input().split())
uf = DSU(N+1)
for _ in range(Q):
    q, x, y = map(int,input().split())
    if q == 1:
        uf.merge(x, y)
    else:
        x = uf.find(x)
        try:
            print(uf.top[x][y-1])
        except IndexError:
            print(-1)