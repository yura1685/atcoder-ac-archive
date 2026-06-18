S, P = map(int,input().split())
if S*S-4*P < 0:
    print('No')
    exit()
D = (S*S - 4*P)**(1/2)
if int(D) != D:
    print('No')
    exit()
if S - D <= 0:
    print('No')
else:
    print('Yes')