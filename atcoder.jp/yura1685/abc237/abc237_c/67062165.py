S = list(input())
cnt = 0
while S and S[-1] == 'a':
    S.pop()
    cnt += 1
S.reverse()
tnc = 0
while S and S[-1] == 'a':
    S.pop()
    tnc += 1
if tnc > cnt:
    print('No')
    exit()
n = len(S)
for i in range(n):
    if S[i] != S[n-1-i]:
        print('No')
        exit()
print('Yes')