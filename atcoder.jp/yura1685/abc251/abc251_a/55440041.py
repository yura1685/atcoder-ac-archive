S = input()
a = []
a += [S] * (6 // len(S))
b = ''.join(a)
print(b)