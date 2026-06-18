N = int(input())
reach = 0
for i in range(N):
    D1, D2 = map(int,input().split())
    if D1 == D2:
        reach += 1
    elif D1 != D2:
        reach = 0
    if reach == 3:
        print('Yes')
        exit()
print('No')