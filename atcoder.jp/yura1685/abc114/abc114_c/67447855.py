from itertools import product

N = int(input())

ans = 0
for i in range(3,len(str(N))+2):
    for n in product('357',repeat=i):
        n = ''.join(n)
        if n.count('3') > 0 and n.count('5') > 0 and n.count('7') > 0:
            if int(n) <= N:
                ans += 1

print(ans)