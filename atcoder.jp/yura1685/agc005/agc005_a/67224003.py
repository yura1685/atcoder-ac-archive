X = input()

stuck = []
for x in X:
    if x == 'S':
        stuck.append(x)
    else:
        if stuck and stuck[-1] == 'S':
            stuck.pop()
        else:
            stuck.append(x)

print(len(stuck))