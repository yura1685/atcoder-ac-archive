S = input()
push, reach = 0, 0
for i in range(len(S)):
    if S[i] != '0':
        if reach == 1:
            push += 2
            reach = 0
        elif reach == 0:
            push += 1
    elif S[i] == '0':
        if reach == 1:
            push += 1
            reach = 0
        elif i == len(S)-1:
            push += 1
        else:
            reach = 1

print(push)