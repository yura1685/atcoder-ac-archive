import sys
sys.set_int_max_str_digits(0)

N = int(input())
A = input()
B = input()
C = []
D = []

for i in range(N):
    min_digit = min(int(A[i]), int(B[i]))
    max_digit = max(int(A[i]), int(B[i]))
    C.append(str(min_digit))
    D.append(str(max_digit))

c = int(''.join(C))
d = int(''.join(D))

M = 998244353

result = ((c % M) * (d % M)) % M

print(result)