n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
a_c = 0
b_c = 0
while a_c != n and b_c != m:
    if a[a_c] < b[b_c]:
        c.append(a[a_c])
        a_c += 1
    elif a[a_c] > b[b_c]:
        c.append(b[b_c])
        b_c += 1
    elif a[a_c] == b[b_c]:
        a_c += 1
        b_c += 1

if a_c == n:
    while b_c != m:
        c.append(b[b_c])
        b_c += 1

elif b_c == m:
    while a_c != n:
        c.append(a[a_c])
        a_c += 1

print(*c)