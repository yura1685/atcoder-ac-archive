S = input()
c = ''
d = ['A','C','G','T']
for i in S:
    if i in d:
        c += 'O'
    else:
        c += 'X'
p = list(map(str,c.split('X')))
ans = 0
for i in p:
    ans = max(ans,len(i))
print(ans)