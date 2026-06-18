S = input()
Q = int(input())
d = {'A':'BC', 'B':'CA', 'C':'AB'}

def dfs(t,k):
    if t == 0: return S[k]
    if k == 0:
        if S[0] == 'A':
            return ['A', 'B', 'C'][t % 3]
        if S[0] == 'B':
            return ['B', 'C', 'A'][t % 3]
        if S[0] == 'C':
            return ['C', 'A', 'B'][t % 3]
    return d[dfs(t-1,k//2)][k % 2]

for _ in range(Q):
    t, k = map(int,input().split())
    print(dfs(t,k-1))