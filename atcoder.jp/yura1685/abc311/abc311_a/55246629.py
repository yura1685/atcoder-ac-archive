N = int(input())
S = input()
a, b, c = 0, 0, 0
j = 0
while a == 0 or b == 0 or c == 0:
    if S[j] == 'A':
        a += 1
    if S[j] == 'B':
        b += 1
    if S[j] == 'C':
        c += 1
    j += 1
print(a+b+c)