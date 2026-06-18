n = int(input())
a = list(map(int,input().split()))
d = set(a)
for i in range(2001):
    if i not in d:
        print(i)
        exit()