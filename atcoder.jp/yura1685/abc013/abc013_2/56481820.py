a = int(input())
b = int(input())

if a < b:
    print(min(-a+b,10+a-b))
else:
    print(min(a-b,10-a+b))