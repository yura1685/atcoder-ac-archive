S = list(input())
S = list(reversed(S))
n = 0
ABC = 0
alp = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n < len(S):
    ABC += alp.index(S[n])*26**n
    n += 1
print(ABC)