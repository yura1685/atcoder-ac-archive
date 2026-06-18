N, Q = map(int, input().split())

SIZE = [1] * N
LEADER = list(range(N))
MEMBER = [set([i]) for i in range(N)]
COLOR = [0] * N
BLACK = [0] * N

ans = 0
flag = False
for _ in range(Q):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if flag:
        print(-1)
        continue

    Lu, Lv = LEADER[u], LEADER[v]
    if Lu == Lv:
        if COLOR[u] != COLOR[v]:
            print(ans)
        else:
            flag = True
            print(-1)
    else:
        if SIZE[Lu] < SIZE[Lv]:
            Lu, Lv = Lv, Lu
        ans -= min(BLACK[Lu], SIZE[Lu] - BLACK[Lu])
        ans -= min(BLACK[Lv], SIZE[Lv] - BLACK[Lv])
        FLIP = (COLOR[u] == COLOR[v])
        for Kv in MEMBER[Lv]:
            if FLIP:
                COLOR[Kv] ^= 1
            LEADER[Kv] = Lu
            if COLOR[Kv] == 1:
                BLACK[Lu] += 1
            MEMBER[Lu].add(Kv)
        MEMBER[Lv].clear()
        SIZE[Lu] += SIZE[Lv]
        ans += min(BLACK[Lu], SIZE[Lu] - BLACK[Lu])
        print(ans)