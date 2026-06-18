def solve():
    N = int(input())
    S = input()
    danger = set(i+1 for i in range(2**N-1) if S[i] == '1')
    s = set([0])
    for _ in range(N):
        new_set = set()
        for saf in s:
            for i in range(N):
                if (saf >> i) & 1 == 0:
                    x = saf + 2**i
                    if x not in danger:
                        new_set.add(x)
        s = new_set.copy()
    print('Yes' if s else 'No')

T = int(input())
for _ in range(T):
    solve()