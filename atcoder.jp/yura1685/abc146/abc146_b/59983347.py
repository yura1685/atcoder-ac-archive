N = int(input())
S = input()
c = ''
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in S:
    c += alp[alp.index(i)+N]
print(c)