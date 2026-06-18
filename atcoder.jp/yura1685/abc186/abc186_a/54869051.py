N , W = map(int, input().split())
total = 0
c = 0
while total <= N:
    total = total + W
    c = c + 1
print (c - 1)