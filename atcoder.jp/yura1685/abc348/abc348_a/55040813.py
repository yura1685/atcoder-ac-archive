N = int(input())
S = ['o']
S = S * N
for i in range(N):
    if (i+1) % 3 == 0:
        S[i] = 'x'
S = ''.join(S)
print(S)