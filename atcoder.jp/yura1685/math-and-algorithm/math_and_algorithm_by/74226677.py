a, b, c = map(int, input().split())
if c == 1: exit(print('No'))
L, R = a, 1
while b and L >= R:
    R *= c 
    b -= 1
print('Yes' if L < R else 'No')