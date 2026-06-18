from collections import deque
import bisect

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())
ch = [0]*(X+1); ch[0] = 1


d = deque([0])
while d:
    c = d.popleft()
    for a in A:
        b = c+a
        if b == X:
            print('Yes')
            exit()
        if b > X:
            break
        if bisect.bisect(B,b) == bisect.bisect_left(B,b):
            if ch[b] == 0:
                ch[b] = 1
                d.append(b)
print('No')