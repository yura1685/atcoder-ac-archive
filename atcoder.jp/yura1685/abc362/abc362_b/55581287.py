ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
if (bx-ax)*(cx-ax)+(by-ay)*(cy-ay) == 0:
    print('Yes')
    exit()
if (ax-bx)*(cx-bx)+(ay-by)*(cy-by) == 0:
    print('Yes')
    exit()
if (bx-cx)*(ax-cx)+(by-cy)*(ay-cy) == 0:
    print('Yes')
    exit()
print('No') 