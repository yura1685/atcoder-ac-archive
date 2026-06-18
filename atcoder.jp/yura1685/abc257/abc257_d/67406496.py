from collections import deque

N = int(input())
xyp = [tuple(map(int,input().split())) for _ in range(N)]

def f(S): # ジャンプ力Sで全ての頂点から行けるか？
    for s in range(N): # スタート地点
        d = deque([s])
        cnt = 0
        c = [0]*N; c[s] = 1
        while d:
            u = d.popleft()
            cnt += 1
            xu, yu, pu = xyp[u]
            for v in range(N):
                if c[v]:
                    continue
                xv, yv, pv = xyp[v]
                if abs(xu-xv) + abs(yu-yv) <= pu*S:
                    c[v] = 1
                    d.append(v)
        if cnt == N:
            return True
    return False

l, r = 0, 10**10
while r - l > 1:
    mid = (l+r)//2
    if f(mid):
        r = mid
    else:
        l = mid

print(r)