N, L = map(int,input().split())
A = list(map(int,input().split()))

seat = L
left = 0
ans = True

for a in A:
    if a == 1:
        if seat == 0:
            left -= 1
        elif seat == 1:
            seat -= 1
        else:
            seat -= 2
            left += 1
    else:
        if seat <= 1:
            ans = False
        elif seat == 2:
            seat -= 2
        else:
            seat -= 3
            left += 1

print('Yes' if ans else 'No')