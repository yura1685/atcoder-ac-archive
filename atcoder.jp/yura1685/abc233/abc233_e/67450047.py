import sys
sys.set_int_max_str_digits(0)


I = input()
s = sum((int(a) for a in I))
X = int(I)
print((X * 10 - s) // 9)