a, b = map(int,input().split())
if 0 < a:
    print('Positive')
elif a <= 0 <= b:
    print('Zero')
else:
    c = b - a
    if c % 2 == 0:
        print('Negative')
    else:
        print('Positive')