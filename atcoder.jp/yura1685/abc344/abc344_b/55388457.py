L = []
while True:
    a = int(input())
    L.append(a)
    if a == 0:
        break

for i in list(reversed(L)):
    print(i)