deg, dis = map(int,input().split())
huko = ['N','NNE','NE','ENE','E','ESE','SE','SSE',
        'S','SSW','SW','WSW','W','WNW','NW','NNW','N']
deg = int((deg + 112.5) // 225)

gomi = [(0,12),(18,90),(96,198),(204,324),(330,474),(480,642),
        (648,828),(834,1026),(1032,1242),(1248,1464),
        (1470,1704),(1710,1956),(1962,10**8)]

if dis % 6 < 3:
    dis = (dis//6)*6
else:
    dis = ((dis+5)//6)*6

for i in range(13):
    if gomi[i][0] <= dis <= gomi[i][1]:
        ind = i

if ind == 0:
    print('C',0)
else:
    print(huko[deg], ind)