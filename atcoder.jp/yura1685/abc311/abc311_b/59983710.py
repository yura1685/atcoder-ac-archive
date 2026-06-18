N, D = map(int,input().split())
c = ['o']*D
for i in range(N):
    S = input()
    for i in range(D):
        if S[i] == 'x':
            c[i] = 'x'

p = ''
for i in c:
    p += i
q = list(map(str,p.split('x')))
ans = 0
for i in q:
    ans = max(ans,len(i))
print(ans)