a, b, k = map(int,input().split())
shout = 0
while a < b:
    a *= k
    shout += 1
print(shout)