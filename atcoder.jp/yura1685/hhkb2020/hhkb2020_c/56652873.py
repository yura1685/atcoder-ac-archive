N = int(input())
p = list(map(int,input().split()))
s = set()
min_p = 0
for x in p:
    s.add(x)
    while True:
        if min_p in s:
            min_p += 1
        else:
            print(min_p)
            break