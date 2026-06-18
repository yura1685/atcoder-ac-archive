A, B = map(int,input().split())

x = int((A/(2*B))**(2/3)) - 1

def fall(n):
    return A/((1+n)**0.5) + n*B

if x < 0:
    print(fall(0))
    exit()

n1, n2 = x, x+1
print(min(fall(n1), fall(n2)))