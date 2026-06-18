N = int(input())
A = list(map(int,input().split()))

s = set(A)

for a in A:
    if a+3 in s and a+6 in s:
        print('Yes')
        exit()
print('No')