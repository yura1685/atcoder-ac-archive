from collections import Counter

N = int(input())
A = list(map(int,input().split()))
L = Counter(A)

stick = []
for i in L:
    if 2 <= L[i] <= 3:
        stick.append(i)
    elif 4 <= L[i]:
        stick.append(i)
        stick.append(i)
stick = sorted(stick)

if 0 <= len(stick) <= 1:
    print(0)
else:
    print(stick[-1]*stick[-2])