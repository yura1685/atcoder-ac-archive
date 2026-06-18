N, M = map(int,input().split())
A = list(map(int,input().split()))

correct = -1
lead = 0
for a in A:
    if lead == 0:
        correct = a
        lead += 1
    elif correct == a:
        lead += 1
    else:
        lead -= 1

count = 0
for a in A:
    if a == correct:
        count += 1
print(correct if 2*count > N else '?')