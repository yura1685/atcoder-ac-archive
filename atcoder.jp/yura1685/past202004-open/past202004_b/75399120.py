s = input()
a,b,c=s.count('a'), s.count('b'), s.count('c')
m=max(a,b,c)
print('a' if a==m else 'b' if b==m else 'c')