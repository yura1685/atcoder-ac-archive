a, b, c, d = map(int,input().split())
time = 0
for i in range(101):
    if a <= i < b and c <= i < d:
        time += 1
print(time)