N, M = map(int,input().split())
prob = list(map(int,input().split()))
cawa = []
score = []
for i in range(N):
    S = input()
    poi = i+1
    for i in range(M):
        if S[i] == 'o':
            poi += prob[i]
    score.append(poi)
    cawa.append(S)

for coder in range(N):
    point = score[coder]
    other_max = max(score[:coder] + score[coder+1:])
    if point > other_max:
        print(0)
    elif point == other_max:
        print(1)
    else:
        unsolved = []
        p = cawa[coder]
        for i in range(M):
            if p[i] == 'x':
                unsolved.append(prob[i])
        unsolved = sorted(unsolved, reverse=True)
        should_solve = 0
        count = 0
        while point <= other_max:
            point += unsolved[count]
            should_solve += 1
            count += 1
        print(should_solve)