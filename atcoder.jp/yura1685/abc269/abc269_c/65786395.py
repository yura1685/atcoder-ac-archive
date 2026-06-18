import itertools
n= int(input())

def f(n):
    return [int(digit) for digit in bin(n)[2:]]
def bit(n):
    return list(itertools.product([0, 1], repeat=n))
def lo_to_2(A):
    ans = 0
    n = len(A)
    for i in range(1,n+1):
        ans += A[-i]*2**(i-1)
    return ans

n2 = f(n)
digit1 = []
for i in range(len(n2)):
    if n2[i] == 1:
        digit1.append(i)

allbit = bit(len(digit1))
for x in allbit:
    for y in range(len(digit1)):
        n2[digit1[y]] = x[y]
    print(lo_to_2(n2))