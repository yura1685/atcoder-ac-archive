N, M = map(int,input().split())
S = input()
T = input()
ans = 3
if T[:N] == S:
    ans -= 2
if T[-N:] == S:
    ans -= 1
print(ans)