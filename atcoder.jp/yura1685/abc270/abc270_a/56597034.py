a, b = map(int,input().split())
Taka, Aoki = [0]*3, [0]*3
if a >= 4:
    Taka[0] = 1
if a % 2 == 1:
    Taka[2] = 1
if b >= 4:
    Aoki[0] = 1
if b % 2 == 1:
    Aoki[2] = 1
Taka[1] = a - 4*Taka[0] - Taka[2]
Aoki[1] = b - 4*Aoki[0] - Aoki[2]
Sunu = [0]*3
for i in range(3):
    if Taka[i] == 0 and Aoki[i] == 0:
        Sunu[i] = 0
    else:
        Sunu[i] = 1
print(4*Sunu[0] + 2*Sunu[1] + Sunu[2])