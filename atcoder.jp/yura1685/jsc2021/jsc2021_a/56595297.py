x, y, z = map(int,input().split())
takahashi = y/x
nedan = 1
while nedan / z < takahashi:
    nedan += 1
print(nedan-1)