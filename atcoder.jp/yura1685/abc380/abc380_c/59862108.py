N, K = map(int,input().split())
S = input()
p = 0
l, r = 0, 0
count = 0
for i in range(N):
    if S[i] == '1' and count == 0:
        count = 1
        p += 1
        if p == K-1:
            l = i
        
    if S[i] == '0':
        if p == K and count == 1:
            r = i-1
        count = 0
    
if S[-1] == '1' and p == K:
    r = N-1

s = S[l:r+1]
s0 = s.count('0')
s1 = s.count('1')
x = '1'*s1 + '0'*s0

print(S[:l] + x + S[r+1:])