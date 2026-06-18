N = int(input())
rt = int(N**(1/2)) + 5
prime = [False,False] + [True]*(rt+5)
for i in range(2,rt+7):
    p = prime[i]
    if not p:
        continue
    for q in range(i*2,rt+7,i):
        prime[q] = False

for i in range(2,rt):
    p = prime[i]
    if not p:
        continue
    while N % i == 0:
        N //= i
        print(i,end=' ')

if N > 1:
    print(N)