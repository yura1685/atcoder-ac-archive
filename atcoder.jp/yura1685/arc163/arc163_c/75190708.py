ans = [[], [1], [], [2,3,6]]
for _ in range(500):
    L = ans[-1].copy()
    for x in L:
        if not (x+1 in L or x*(x+1) in L):
            L.remove(x)
            L.append(x+1)
            L.append(x*(x+1))
            break
    ans.append(sorted(L))

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 2:
        print('No')
    else:
        print('Yes')
        print(*ans[N])