def sex(sex1,sex2):
    return (sex1[1]-sex2[1])/(sex1[0]-sex2[0])


sex3 = int(input())
sex4 = []
for sex5 in range(sex3):
    sex6, sex7 = map(int,input().split())
    sex4.append([sex6,sex7])

sex8 = 0
if len(sex4) == 1:
    print(0)
    exit()
for sex9 in range(sex3-1):
    for sex10 in range(sex9+1,sex3):
        if -1 <= sex(sex4[sex9],sex4[sex10]) <= 1:
            sex8 += 1
print(sex8)