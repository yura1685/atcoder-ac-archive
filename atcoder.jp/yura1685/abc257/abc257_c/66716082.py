from bisect import bisect_left

N = int(input())
S = input()
W = list(map(int,input().split())) + [0]

kid = [W[i] for i in range(N) if S[i] == '0']
man = [W[i] for i in range(N) if S[i] == '1']
W.sort(); kid.sort(); man.sort()
m = len(man)
ans = 0
for x in W:
    yura = bisect_left(kid,x) + m - bisect_left(man,x)
    yura1 = bisect_left(kid,x+1) + m - bisect_left(man,x+1)
    ans = max(ans,yura,yura1)

print(ans)