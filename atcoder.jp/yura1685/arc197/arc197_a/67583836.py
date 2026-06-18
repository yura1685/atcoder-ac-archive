T = int(input())

def solve():
    H, W = map(int,input().split())
    S = input()
    D = S.count('D')
    R = S.count('R')
    D, R = H-D-1, W-R-1 # 配置できるD,Rの数
    ans = 0
    q = 0
    for i in range(H+W-2):
        if S[i] == '?':
            q += 1
        ans += min(D,q) - max(q-R,0) + 1
    print(ans+1)

for _ in range(T):
    solve()