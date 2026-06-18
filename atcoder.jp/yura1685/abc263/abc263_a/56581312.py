L = list(map(int,input().split()))
if len(set(L)) == 2:
    if L.count(L[0]) == 2 or L.count(L[0]) == 3:
        print('Yes')
        exit()
print('No')