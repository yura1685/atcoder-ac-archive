def nisinsuu(n):
    return [int(digit) for digit in bin(n)[2:]]

K = int(input())
d = {1:'2', 0:'0'}
X = ''
for i in nisinsuu(K):
    X += d[i]
print(int(X))