def check(S : str):
    R = list(S)
    L = list(reversed(R))
    return R == L

S = input()
n = len(S)
T = S[:n//2]
if check(S) and check(T):
    print('Yes')
else:
    print('No')