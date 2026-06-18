S = input() + 'XX'
N = len(S)

joi, ioi = 0, 0
for i in range(N-2):
    if S[i:i+3] == 'JOI':
        joi += 1
    if S[i:i+3] == 'IOI':
        ioi += 1

print(joi)
print(ioi)