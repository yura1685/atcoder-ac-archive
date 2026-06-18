R, C = map(int,input().split())
R, C = abs(8-R), abs(8-C)
R, C = max(R,C), min(R,C)
if R % 2 == 1:
    print('black')
else:
    print('white')