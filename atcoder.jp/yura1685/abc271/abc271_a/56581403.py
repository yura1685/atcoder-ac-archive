n = int(input())
d = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
a = n // 16
b = n % 16
if a >= 10:
    a = d[a]
if b >= 10:
    b = d[b]
print(str(a)+str(b))