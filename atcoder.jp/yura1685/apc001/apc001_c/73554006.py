N = int(input())
l, r, m = 0, N-1, N//2
print(l); L = input()
if L == 'Vacant': exit()
print(r); R = input()
if R == 'Vacant': exit()
print(m); M = input()
if M == 'Vacant': exit()

while 1:
    B1, B2 = (L != M), (m-l-1) % 2
    if B1 ^ B2:
        l, r = m, r
        L, R = M, R        
    else:
        l, r = l, m
        L, R = L, M
    m = (l+r)//2
    print(m); M = input()
    if M == 'Vacant': break