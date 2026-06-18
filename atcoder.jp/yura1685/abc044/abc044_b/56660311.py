from collections import Counter
w = Counter(input())
for i in w:
    if w[i] % 2 == 1:
        print('No');exit()
print('Yes')