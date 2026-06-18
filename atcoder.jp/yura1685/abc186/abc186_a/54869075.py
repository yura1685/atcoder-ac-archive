N , W = map(int, input().split())
total = 0
while total <= N:
    total = total + W
print (total//W - 1)