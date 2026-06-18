a,b = map(int,input().split())
c = input().split()
d = []
for i in range(a):
    food = input().split()
    d.append(food)
intake = []
for i in range(b):
    xi = 0
    for j in range(a):
        xi += int(d[j][i])
    intake.append(xi)
achieves = 0
for i in range(b):
    if int(c[i]) <= int(intake[i]):
        achieves += 1
if achieves == b:
    print("Yes")
else:
    print("No")