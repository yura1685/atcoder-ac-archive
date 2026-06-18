from sympy.ntheory import factorint

N = int(input())

p = factorint(N)

if N == 1:
    print('Not Prime')
    exit()
if len(p) == 1:
    for i in p:
        if p[i] == 1:
            print('Prime')
            exit()
if (2 not in p and 3 not in p and 5 not in p):
    print('Prime')
    exit()
print('Not Prime')