H = int(input())
m = 1
while H != 1:
    H //= 2; m += 1
print(2**m-1)