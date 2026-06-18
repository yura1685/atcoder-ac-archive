N = int(input())
roulette = [[] for _ in range(37)]
man = []
for i in range(N):
    c = int(input())
    A = list(map(int,input().split()))
    for a in A:
        roulette[a].append((c,i+1))
X = int(input())
atari = sorted(roulette[X])
winner = 0
if atari == []:
    print(0)
    exit()
c = atari[0][0]
hoge = []    
for m in atari:
    if m[0] == c:
        winner += 1
        hoge.append(m[1])
print(winner)
print(*hoge)