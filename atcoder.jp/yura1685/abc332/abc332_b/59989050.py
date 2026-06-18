def solve(K,G,M):
    g_now, m_now = 0, 0
    for i in range(K):
        if g_now == G:
            g_now = 0
        elif m_now == 0:
            m_now = M
        else:
            if G - g_now >= m_now:
                g_now += m_now 
                m_now = 0
            else:
                m_now -= G - g_now
                g_now = G
    print(g_now, m_now)


K, G, M = map(int,input().split())
solve(K,G,M)