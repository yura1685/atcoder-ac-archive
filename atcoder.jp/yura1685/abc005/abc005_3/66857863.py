from collections import deque
T = int(input())
N = int(input())
A = list(map(lambda x:(int(x)+T,int(x)),input().split()))
A.sort()
M = int(input())
B = list(map(int,input().split()))

eat = 0
for b in B:
    for e, s in A:
        if s <= b <= e:
            A.pop(0)
            eat += 1
            break           
        if len(A) == 0:
            print('no')
            exit()
print('yes' if eat==M else 'no')