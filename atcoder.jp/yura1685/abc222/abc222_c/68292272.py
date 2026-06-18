N, M = map(int,input().split())
hand = [input() for _ in range(2*N)]
rank = [[0,i] for i in range(2*N)]

for m in range(M):
    for i in range(N):
        n1, n2 = rank[2*i][1], rank[2*i+1][1]
        h1, h2 = hand[n1][m], hand[n2][m]
        if (h1,h2) in [('G','C'),('P','G'),('C','P')]:
            rank[2*i][0] -= 1
        if (h1,h2) in [('C','G'),('G','P'),('P','C')]:
            rank[2*i+1][0] -= 1
    rank.sort()
 
for i in rank:
    print(i[1]+1)