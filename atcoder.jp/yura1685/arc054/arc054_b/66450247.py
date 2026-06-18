import math

P = float(input())
a = math.log(2)
a = 2*P*a/3
x = 3*math.log2(a)/2

hoge = x+P/(2**(2*x/3))
print(hoge if x > 0 else P)