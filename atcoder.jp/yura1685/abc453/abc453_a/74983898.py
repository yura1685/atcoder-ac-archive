N = int(input())
S = list(input())
while S and S[0] == 'o':
  S.pop(0)
print(''.join(S))