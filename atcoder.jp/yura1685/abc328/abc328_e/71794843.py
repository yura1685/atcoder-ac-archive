def get_permutations(n, m):
    result = []
    # 文字列ではなく、文字のリストを使い回す
    current_path = [None] * (n + m)

    def backtrack(ones_left, zeros_left, index):
        if ones_left == 0 and zeros_left == 0:
            # 最後に一気に結合して文字列にする
            result.append("".join(current_path))
            return
        
        if zeros_left > 0:
            current_path[index] = "0"
            backtrack(ones_left, zeros_left - 1, index + 1)
            
        if ones_left > 0:
            current_path[index] = "1"
            backtrack(ones_left - 1, zeros_left, index + 1)

    backtrack(n, m, 0)
    return result

N, M, K = map(int,input().split())
g = []
W = []
for i in range(M):
    u, v, w = map(int,input().split())
    g.append((u-1,v-1))
    W.append(w%K)

from atcoder.dsu import DSU

ans = K
X = get_permutations(N-1,M-N+1)
for P in X:
    s = set()
    C = []
    for i in range(M):
        if P[i] == '1':
            s.add(g[i][0])
            s.add(g[i][1])
            C.append(i)
    if len(s) < N:
        continue
    uf = DSU(N)
    for i in C:
        uf.merge(g[i][0], g[i][1])
    if uf.size(0) != N: continue
    score = sum(W[i] for i in C)
    ans = min(ans, score % K)

print(ans)