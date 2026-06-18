A, B = map(int,input().split())
if A == B:
    print(1)
elif (B-A) % 2 == 0:
    print(3)
else:
    print(2)