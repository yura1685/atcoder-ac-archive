N = int(input())
S = str(input())
T = str(input())
aoi, bi = 0, 0
for i in range(N):
    if S[i] == 'R' and T[i] == 'P':
        bi += 1
    elif S[i] == 'S':
        if T[i] == 'R':
            bi += 1
        else:
            aoi += 1
print(aoi,bi)