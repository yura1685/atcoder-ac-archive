H = int(input())
plantheight = 0
Day = 0
while plantheight <= H:
    plantheight += 2**Day
    Day += 1
print(Day)