def base_repr(num, base):
    digits = '012'
    res = []
    while num:
        res.append(digits[num % base])
        num //= base
    res = [int(x) for x in res]
    return res

def solve():
    N, K = map(int,input().split())
    M = base_repr(N, 3)
    S = sum(M)
    if S > K: return False
    if S == K: return True
    nokori = K - S
    if nokori % 2: return False
    if N - M[0] >= nokori: return True
    return False

for _ in range(int(input())):
    print('Yes' if solve() else 'No')