x1, y1, x2, y2 = map(int,input().split())
def sqrt5(x,y):
    return [(x-2,y+1),(x-2,y-1),(x-1,y+2),(x-1,y-2),(x+1,y+2),(x+1,y-2),(x+2,y+1),(x+2,y-1)]

j = sqrt5(x2,y2)
for i in sqrt5(x1,y1):
    if i in j:
        print('Yes')
        exit()
print('No')