S = input()
Q = int(input())
K = [int(x) for x in input().split()]
l = len(S)

for k in K:
    alp = S[(k-1) % l]
    rev = 0
    n = (k-1)//l
    for i in range(59,-1,-1):
        if n // (2**i) == 1:
            rev += 1
            n %= 2**i
    if rev % 2 == 1:
        if alp.islower():
            alp = alp.upper()
        else:
            alp = alp.lower()
    print(alp,end=' ')