X, Y = map(int,input().split())
nokori = Y-X
if nokori <= 0:
    print(0)
elif nokori % 10 == 0:
    print(nokori // 10)
else:
    print(nokori // 10 +1)