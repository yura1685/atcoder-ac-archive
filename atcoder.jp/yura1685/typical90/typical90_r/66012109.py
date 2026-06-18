import math

T = int(input())
L, X, Y = map(int,input().split())

def P(e):
    theta = 2*math.pi*e/T
    return -L/2*math.sin(theta), L/2*(1-math.cos(theta))



Q = int(input())
for _ in range(Q):
    E = int(input())
    p_y, p_z = P(E)
    bunbo = X**2 + (Y-p_y)**2
    bunbo = bunbo**(0.5)
    bunsi = p_z
    print(math.degrees(math.atan(bunsi/bunbo)))