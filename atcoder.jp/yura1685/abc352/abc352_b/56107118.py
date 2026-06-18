S = input()
T = input()
right_type = []
a = 0
for i in range(len(T)):
    if T[i] == S[a]:
        right_type.append(str(i+1))
        a += 1
print(*right_type)