N = int(input())
H = list(map(int,input().split()))
S = ''

for i in range(N-1):
    if H[i] >= H[i+1]:
        S += '1'
    else:
        S += '0'

ans = 0
c = list(map(str,S.split('0')))
if len(c) == 0:
    print(0)
else:
    print(len(max(c)))