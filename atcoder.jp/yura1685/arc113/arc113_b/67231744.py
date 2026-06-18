A, B, C = map(int,input().split())

a = A % 10

if a in [0,1,5,6]:
    print(a)
    exit()

if a in [3,7,9]:
    if a == 3 or a == 7:
        print(a**pow(B,C,4) % 10)
    elif a == 9:
        print(9**pow(B,C,2) % 10)
    exit()

if a == 2:
    print(2**(pow(B,C,4)+4) % 10)
if a == 4:
    print(4**(pow(B,C,2)+2) % 10)
if a == 8:
    print(8**(pow(B,C,4)+4) % 10)