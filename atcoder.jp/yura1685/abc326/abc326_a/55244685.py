X, Y = map(int, input().split())
if 1 <= Y - X <= 2:
    print('Yes')
elif 1 <= X - Y <= 3:
    print('Yes')
else:
    print('No')