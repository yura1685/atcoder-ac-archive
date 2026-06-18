S = input()
c00 = S.count('00')
S = S.replace('00','')
print(c00 + len(S))