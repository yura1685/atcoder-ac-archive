S = input()
a = S.index('A')
n = len(S)
for i in range(n):
    if S[n-i-1] == 'Z':
        z = n - i - 1
        break
print(z-a+1)