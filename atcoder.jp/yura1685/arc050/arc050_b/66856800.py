R, B = map(int,input().split())
x, y = map(int,input().split())

def make(num):
    fr = (R-num)//(x-1)
    fb = (B-num)//(y-1)
    if fr + fb >= num:
        return True
    else:
        return False
    
lef, rig = 0, min(R,B)+1
while lef+1 < rig:
    mid = (lef+rig)//2
    if make(mid):
        lef = mid
    else:
        rig = mid

print(lef)