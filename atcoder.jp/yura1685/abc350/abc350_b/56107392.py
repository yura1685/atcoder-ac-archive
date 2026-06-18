N, Q = map(int,input().split())
treatment = list(map(int,input().split()))
teeth = [1] * N
for i in treatment:
    if teeth[i-1] == 1:
        teeth[i-1] = 0
    elif teeth[i-1] == 0:
        teeth[i-1] = 1
print(teeth.count(1))