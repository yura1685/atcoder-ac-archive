A,B,C = map(int,input().split())
ans = [['-','!'],
       ['?','+']]

i, j = 0, 1
if A+B==C:
    i = 1
if A-B == C:
    j = 0
print(ans[i][j])