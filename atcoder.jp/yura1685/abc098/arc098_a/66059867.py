N = int(input())
S = input()

c = [0]*N
c[0] = S.count('W') - (S[0]=='W')

M = c[0]

for i in range(1,N):
    c[i] = c[i-1] + (S[i-1]=='E') - (S[i]=='W')
    M = max(M,c[i])
    
print(N-M-1)