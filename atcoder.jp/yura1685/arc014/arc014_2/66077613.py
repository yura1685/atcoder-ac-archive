N = int(input())
word = [input()]
d = {1:'LOSE', 0:'WIN'}

for i in range(N-1):
    c = input()
    if word[-1][-1] != c[0]:
        print(d[i%2])
        exit()
    if c in word:
        print(d[i%2])
        exit()
    word.append(c)

print('DRAW')