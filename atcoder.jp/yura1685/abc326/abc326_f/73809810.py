# s1 + s2 - (S-s1-s2) = target?
# s1 + s2 = (S + target) / 2
# s2 = (S + target) / 2 - s1

def get_sub(idx, sum, mask, L):
    if idx == len(L):
        return [(sum, mask)]
    else:
        # L[idx]を選ばない/選ぶ場合
        return get_sub(idx+1, sum, mask, L) + \
               get_sub(idx+1, sum+L[idx], mask | (1 << idx), L)

def solve(L, target):
    S = sum(L)
    if (S - target) % 2: return -1
    neg = (S - target) // 2 # <--これ何？
    if not 0 <= neg <= S: return -1
    n = len(L)
    L1, L2 = L[:n//2], L[n//2:]
    sub1, sub2 = get_sub(0, 0, 0, L1), get_sub(0, 0, 0, L2)
    set2 = set(s for s, _ in sub2)
    for s, m in sub1:
        if neg - s in set2:
            m2 = sub2[[s for s, _ in sub2].index(neg-s)][1]
            return m | (m2 << (n//2))
    return -1

N, X, Y = map(int,input().split())
A = list(map(int,input().split()))
AX, AY = A[1::2], A[::2]
mx, my = solve(AX, X) * 2, solve(AY, Y)
if mx < 0 or my < 0:
    print('No')
else:
    print('Yes')
    ans = ''
    # これは何？
    for i in range(N):
        if i % 2 == 0:
            if (mx >> i // 2 & 1) + (my >> i // 2 & 1) == 1:
                ans += 'R'
            else:
                ans += 'L'
        else:
            if (mx >> (i + 1) // 2 & 1) ^ (my >> i // 2 & 1) == 1:
                ans += 'L'
            else:
                ans += 'R'
    print(ans)