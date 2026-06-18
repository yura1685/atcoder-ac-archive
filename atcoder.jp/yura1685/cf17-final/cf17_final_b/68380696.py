S = input()
a, b, c = S.count('a'), S.count('b'), S.count('c')
print('YES' if max(a,b,c) - min(a,b,c) <= 1 else 'NO')