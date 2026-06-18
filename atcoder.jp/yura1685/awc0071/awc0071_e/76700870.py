from collections import deque

class MFGraph[T]:
    '''
    maxflow for codon
    Dinic法を用い、頂点数N・辺数MとしてO(N^2 M)で最大流を計算します。

    N: 頂点数
    '''
    N: int
    M: int
    _edge: list[int]
    _capa: list[T]
    __slots__ = ('N', 'M', '_edge', '_capa')
    def __init__(self, N: int) -> None:
        assert 0 <= N < 1 << 30
        self.N: int = N
        self.M: int = 0
        self._edge: list[int] = []
        self._capa: list[T] = []
    #内部関数
    def _make_inf(self) -> T:
        if isinstance(T, int) or isinstance(T, Int):
            n: T = T(1)
            while n > T(0):
                n <<= T(1)
            return n - T(1)
        elif isinstance(T, UInt):
            return T(-1)
        else:
            return T(1e1000)  #動作不良時は return _float_inf(T(1), T(0)) を試す
    @pure
    @llvm
    def _float_inf[U](self, one: U, zero: U) -> U:  #1.0 / 0.0 = inf によるinf生成
        %inf = fdiv {=U} %one, %zero
        ret {=U} %inf
    def _build_forward_star(self, forward_star_len: int) -> list[i32]:
        assert forward_star_len >= self.N << 1
        fstar: list[i32] = [i32(-1)] * forward_star_len
        for m in range(self.M):
            now, nxt = self._edge[m << 1 | 1] & 0xFFFFFFFF, self._edge[m << 1] & 0xFFFFFFFF
            self._edge[m << 1    ], fstar[now] = int(fstar[now]) << 32 | nxt, i32(m << 1    )
            self._edge[m << 1 | 1], fstar[nxt] = int(fstar[nxt]) << 32 | now, i32(m << 1 | 1)
        return fstar
    def _minimum_cut(self, St: int, permissible_error: T) -> list[bool]:
        fstar: list[i32] = self._build_forward_star(self.N << 1)
        visited: list[bool] = [False] * self.N
        visited[St] = True
        fstar[1] = i32(St << 1)
        d: int = 3
        while d > 1:
            d -= 2
            now: int = int(fstar[d])
            i: int = int(fstar[now])
            while i != -1:
                nxt_i, nxt = self._edge[i] >> 32, self._edge[i] & 0xFFFFFFFF
                if visited[nxt >> 1] == False and self._capa[i] > permissible_error:
                    visited[nxt >> 1] = True
                    fstar[d] = i32(nxt)
                    d += 2
                i: int = nxt_i
        return visited
    def _Dinic(self, St: int, Gl: int, flow_limit: T, pe: T,
               fstar_and_stack: list[i32], flow_and_leak: list[T]) -> T:
        #メンテナンス用メモ: 内部的に頂点は2倍値を使い、配列は以下の通り使い回す
        #E : edge  : int : (nxt_i << 32 | nxt: 2M   )
        #C : capa  : T   : (cap: 2M                 )
        #DFSstack  : i32 : [fstar and dist: 2N  ][DFSstack: N][snapshot: N]
        #flow/leak : T   : [flow and leak: 2N   ]
        if self.M == 0:
            return T(0)
        N, E, C = self.N, self._edge, self._capa
        fstar = dist = stack = snapshot = fstar_and_stack
        for x in range(N):
            snapshot[~ x] = fstar[x << 1]  #snapshot save
        flow = leak = flow_and_leak
        St <<= 1
        Gl <<= 1
        ans: T = T(0)
        while ans < flow_limit:
            #1. BFS
            for x in range(N):
                dist[x << 1 | 1] = i32(N)
                fstar[x << 1] = snapshot[~ x]  #snapshot load
            dist[St | 1] = i32(0)
            stack[N << 1] = i32(St)
            now: int = St
            Lt: int = N << 1
            Rt: int = N << 1 | 1
            while Lt < Rt and now != Gl:
                dist_nxt: i32 = dist[now | 1] + i32(1)
                i: int = int(fstar[now])
                while i != -1:
                    nxt_i, nxt = E[i] >> 32, E[i] & 0xFFFFFFFF
                    if C[i] > pe and dist[nxt | 1] > dist_nxt:
                        dist[nxt | 1] = dist_nxt
                        stack[Rt] = i32(nxt)
                        Rt += 1
                    i: int = nxt_i
                Lt += 1
                now: int = int(stack[Lt])
            if int(dist[Gl | 1]) == N:
                break
            #2. DFS  St ← Glの方向
            flow[Gl], leak[Gl | 1] = flow_limit - ans, T(0)
            stack[N << 1] = i32(Gl)
            d: int = N << 1
            now: int = Gl
            while True:
                if now == Gl and flow[Gl] == leak[Gl | 1]:
                    return ans + leak[Gl | 1]
                if now == St or flow[now] == leak[now | 1]:
                    #[St側] now → back [Gl側] に届いたフローを全部流す
                    current_flow: T = flow[now]
                    d -= 1
                    now: int = int(stack[d])
                    i: int = int(fstar[now])
                    assert 0 <= i < self.M << 2, f'{i = }, {self.M = }'
                    C[i] += current_flow
                    C[i ^ 1] -= current_flow
                    leak[now | 1] += current_flow
                    continue
                #[St側] nxt → now → back [Gl側] に流したい nxt方向に逆辺をたどる
                dist_nxt: i32 = dist[now | 1] - i32(1)
                i: int = int(fstar[now])
                while i != -1:
                    nxt_i, nxt = E[i] >> 32, E[i] & 0xFFFFFFFF
                    rev_cap: T = C[i ^ 1]
                    if dist_nxt == dist[nxt | 1] and rev_cap > pe:
                        flow[nxt] = min(flow[now] - leak[now | 1], rev_cap)
                        leak[nxt | 1] = T(0)
                        fstar[now] = i32(i)
                        d += 1
                        stack[d] = i32(nxt)
                        now: int = nxt
                        break
                    i: int = nxt_i
                else:
                    fstar[now] = i32(-1)
                    current_flow: T = leak[now | 1]
                    if now == Gl:
                        ans += current_flow
                        break
                    d -= 1
                    now: int = int(stack[d])
                    i: int = int(fstar[now])
                    C[i] += current_flow
                    C[i ^ 1] -= current_flow
                    leak[now | 1] += current_flow
                    fstar[now] = i32(E[i] >> 32)
        return ans
    def _maxflow_capacity_scaling(self, St: int, Gl: int, flow_limit: T) -> T:
        if self.M == 0 or flow_limit == T(0):
            return T(0)
        cap_max: T = max(self._capa)
        if cap_max == T(0):
            return T(0)
        scaling: T = T(1)
        while scaling <= (cap_max >> T(1)):
            scaling <<= T(1)
        ans: T = T(0)
        fstar_and_stack: list[i32] = self._build_forward_star(self.N << 2)
        flow_and_leak: list[T] = [T(0)] * (self.N << 1)
        while flow_limit >= T(1) and scaling >= T(1):
            current_flow: T = self._Dinic(St, Gl, flow_limit, scaling - T(1),
                                          fstar_and_stack, flow_and_leak)
            ans += current_flow
            flow_limit -= current_flow
            scaling >>= T(1)
            for x in range(self.N):
                fstar_and_stack[x << 1] = fstar_and_stack[~ x]  #snapshot load
        return ans

    #辺の操作
    def add_edge(self, now: int, nxt: int, cap: T) -> None:
        '頂点nowから頂点nxtに、容量capの辺を追加します。'
        assert 0 <= now < self.N and 0 <= nxt < self.N, f'{now = }, {nxt = }'
        assert T(0) <= cap
        self._edge.append(nxt << 1)
        self._edge.append(now << 1)
        self._capa.append(cap)
        self._capa.append(T(0))
        self.M += 1

    #最大流の実行
    def flow(self, St: int, Gl: int) -> T:
        '頂点Stから頂点Glに最大までフローを流し、流せた量を返します。'
        assert 0 <= St < self.N and 0 <= Gl < self.N
        if self.M == 0:
            return T(0)
        return self._Dinic(St, Gl, self._make_inf(), T(0),
                           self._build_forward_star(self.N << 2),
                           [T(0)] * (self.N << 1))

I = input().split()
N, M = int(I[0]), int(I[1])
g = [[] for _ in range(N+1)]
w = [-1] * (N + 1)
mfg = MFGraph(N + 2)
for _ in range(M):
    I = input().split()
    u, v = int(I[0]), int(I[1])
    g[u].append(v)
    g[v].append(u)

for i in range(1, N+1):
    if w[i] >= 0:
        continue
    w[i] = 0
    dq = deque([i])
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if w[v] == -1:
                w[v] = 1 - w[u]
                dq.append(v)

for u in range(1, N+1):
    if w[u] == 0:
        mfg.add_edge(0, u, 1)
        for v in g[u]:
            mfg.add_edge(u, v, 1)
    else:
        mfg.add_edge(u, N+1, 1)

ans = mfg.flow(0, N+1)
print(ans)