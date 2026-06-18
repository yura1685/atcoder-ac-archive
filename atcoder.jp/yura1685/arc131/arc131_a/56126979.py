A = int(input())
B = int(input())

if B % 2 == 0:
    b = len(str(B))
    x = A * 10**b + B //2
    print(x)

else:
    b = len(str(B))
    x = A * 10**(b+1) + (B//2)*10 + 5
    print(x)