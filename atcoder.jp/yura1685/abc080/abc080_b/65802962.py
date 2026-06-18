S = input()
N = int(S)
s = 0
for i in S:
    s += int(i)
print('Yes' if N % s == 0 else 'No')