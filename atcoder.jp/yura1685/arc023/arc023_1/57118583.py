y = int(input())
m = int(input())
d = int(input())
now = 735369
if m == 1 or m == 2:
    m += 12
    y -= 1
day = 365*y + y//4 - y//100 + y//400 +306*(m+1)//10 + d -429
print(now-day)