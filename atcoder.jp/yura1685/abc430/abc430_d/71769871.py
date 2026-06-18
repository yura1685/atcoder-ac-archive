from sortedcontainers import SortedList

N = int(input())
X = list(map(int,input().split()))
S = SortedList([0])
ans = 2*X[0]
S.add(X[0])
print(ans)
for i in range(1,N):
    x = X[i]
    nex = S.bisect_left(x)
    if len(S) == nex: # 一番右に挿入する場合
        ans -= S[nex-1] - S[nex-2]
        ans += min(S[nex-1]-S[nex-2], x-S[nex-1])
        ans += x - S[nex-1]
    else:
        ans += min(x-S[nex-1],S[nex]-x)
        if nex - 1 == 0:
            ans += x - S[nex]
        else:
            ans -= min(S[nex-1]-S[nex-2], S[nex]-S[nex-1])
            ans += min(S[nex-1]-S[nex-2],x-S[nex-1])
        if nex == len(S) - 1:
            ans += S[nex-1] - x
        else:
            ans -= min(S[nex]-S[nex-1],S[nex+1]-S[nex])
            ans += min(S[nex]-x,S[nex+1]-S[nex])
    S.add(x)
    print(ans)