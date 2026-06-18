from itertools import permutations

N = int(input())
town = [tuple(map(int,input().split())) for _ in range(N)]
C = list(permutations([i for i in range(N)]))

def f(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(0.5)

dis = 0
for c in C:
    for i in range(1,N):
        dis += f(town[c[i-1]][0],town[c[i-1]][1],town[c[i]][0],town[c[i]][1])
print(dis/len(C))