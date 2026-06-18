X = int(input())
c = [i**5 for i in range(120)]

for A5 in c:
    if A5 > X:
        B5 = A5 - X
        if B5 in c:
            print(int(A5**(1/5)),int(B5**(1/5)))
            exit()
    else:
        B5 = X - A5
        if B5 in c:
            print(int(A5**(1/5)),-int(B5**(1/5)))
            exit()