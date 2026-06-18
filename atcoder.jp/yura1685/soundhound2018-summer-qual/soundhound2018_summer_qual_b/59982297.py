S = input()
w = int(input())
n = len(S)

if n % w == 0:
    k = n // w
    c = ''
    for i in range(k):
        c += S[i*w]

else:
    k = n // w
    c = ''
    for i in range(k+1):
        c += S[i*w]

print(c)