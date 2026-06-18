N, T = map(int,input().split())

team = []
for i in range(N):
    A, B = map(int,input().split())
    team.append((-A,B,i))

team.sort()
Ad = -team[0][0]
Bd =  team[0][1]

ans = [0]*N

for a, b, i in team:
    a = -a
    score = T*(Ad-a) + (b-Bd)
    ans[i] = score

for i in range(N):
    print(ans[i])