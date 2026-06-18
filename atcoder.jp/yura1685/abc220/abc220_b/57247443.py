K = int(input())
A, B = map(str,input().split())
p, q = 0, 0
for i in range(len(A)):
    p += int(A[-i-1])*K**(i)
for j in range(len(B)):    
    q += int(B[-j-1])*K**(j)
print(p*q)