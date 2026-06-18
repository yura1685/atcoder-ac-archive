from collections import Counter

def solve():
    S = input()
    cnt = Counter(S)
    M = max(cnt.values())
    if len(S) % 2 == 0 and M  > len(S) // 2:
        print('No')
    elif len(S) % 2 == 1 and M > (len(S) + 1) // 2:
        print('No')
    else:
        print('Yes')
        L = []
        for alp, c in cnt.items():
            L.append((alp, c))
        L.sort(key=lambda x: x[1], reverse=True)
        ans = [None] * len(S)
        idx = 0
        for alp, c in L:
            for _ in range(c):
                ans[idx] = alp
                idx += 2
                if idx >= len(S):
                    idx = 1
        print(''.join(ans))
    
        
for _ in range(int(input())):
    solve()