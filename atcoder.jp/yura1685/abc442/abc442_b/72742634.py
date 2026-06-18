Q = int(input())
sound = 0
stat = 0

for _ in range(Q):
    a = int(input())
    if a == 1:
        sound += 1
    if a == 2:
        sound = max(sound-1, 0)
    if a == 3:
        stat ^= 1
    print('Yes' if (stat and sound >= 3) else 'No')