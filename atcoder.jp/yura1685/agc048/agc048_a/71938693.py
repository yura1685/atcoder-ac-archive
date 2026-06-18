def solve():
    S = input()
    if 'atcoder' < S: return 0
    if S == 'a'*len(S): return -1
    n = 0
    for i in range(len(S)):
        if S[i] != 'a':
            n = i
            break
    if S[n] <= 't': return n
    return n-1

T = int(input())
for _ in range(T):
    print(solve())