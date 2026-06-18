N = int(input())
no1, no2 = 0, 0
no1index = 0
for i in range(1,N+1):
    A = int(input())
    if A >= no1:
        no1, no2 = A, no1
        no1index = i
    elif A >= no2:
        no2 = A

for i in range(1,N+1):
    if i != no1index:
        print(no1)
    else:
        print(no2)