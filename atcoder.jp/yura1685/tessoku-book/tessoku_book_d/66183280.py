N = int(input())
c = bin(N)
s = c[2:]
print('0'*(10-len(s))+s)