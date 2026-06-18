Y = int(input())
uruu = False
if Y % 4 == 0:
    uruu = True
if Y % 100 == 0:
    uruu = False
if Y % 400 == 0:
    uruu = True
print('YES' if uruu == True else 'NO')