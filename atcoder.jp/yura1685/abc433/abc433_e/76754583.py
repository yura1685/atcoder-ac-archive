def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    Max = N * M
    flag = True
    posX = [-1] * (Max + 1)
    posY = [-1] * (Max + 1)
    for i in range(N):
        x = X[i]
        if x > Max or posX[x] != -1:
            flag = False
        if flag:
            posX[x] = i
    for i in range(M):
        y = Y[i]
        if y > Max or posY[y] != -1:
            flag = False
        if flag:
            posY[y] = i
    if not flag:
        print('No')
        return
    ans = [[0] * M for _ in range(N)]
    fixed_rows = []
    fixed_cols = []
    free = []
    for v in range(Max, 0, -1):
        r = posX[v]
        c = posY[v]
        if r != -1 and c != -1:
            for ex_r in fixed_rows:
                free.append((ex_r, c))
            for ex_c in fixed_cols:
                free.append((r, ex_c))
            ans[r][c] = v
            fixed_rows.append(r)
            fixed_cols.append(c)
        elif r != -1 and c == -1:
            if not fixed_cols:
                flag = False
                break
            use_c = fixed_cols[0]
            for ex_c in fixed_cols:
                if ex_c != use_c:
                    free.append((r, ex_c))
            ans[r][use_c] = v
            fixed_rows.append(r)
        elif r == -1 and c != -1:
            if not fixed_rows:
                flag = False
                break
            use_r = fixed_rows[0]
            for ex_r in fixed_rows:
                if ex_r != use_r:
                    free.append((ex_r, c))
            ans[use_r][c] = v
            fixed_cols.append(c)
        else:
            if not free:
                flag = False
                break
            fr, fc = free.pop()
            ans[fr][fc] = v
    if flag:
        print('Yes')
        for a in ans:
            print(*a)
    else:
        print('No')

T = int(input())
for _ in range(T):
    solve()