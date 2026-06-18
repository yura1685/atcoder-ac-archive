from more_itertools import run_length

def remove_kakko(X):
    S = list(run_length.encode(X))
    L = len(S)
    for i in range(L):
        if S[i] == ('x', 2) and 1 <= i < L-1:
            if not (S[i-1][0] == '(' and S[i+1][0] == ')'):
                continue
            l, r = S[i-1][1], S[i+1][1]
            if l == r:
                S[i-1] = ('', 0)
                S[i+1] = ('', 0)
            elif l < r:
                S[i-1] = ('', 0)
                S[i+1] = (')', r-l)
            else:
                S[i-1] = ('(', l-r)
                S[i+1] = ('', 0)
    P = [s*c for s, c in S]
    return ''.join(P)

def solve():
    A = input()
    B = input()
    if remove_kakko(A) == remove_kakko(B):
        print('Yes')
    else:
        print('No')

N = int(input())
for _ in range(N):
    solve()