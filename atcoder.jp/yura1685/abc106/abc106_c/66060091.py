S = input()
K = int(input())


if len(S)>= K:
    if S[:K] == '1'*K:
        print(1)
        exit()

for i in S:
    if i != '1':
        print(i)
        exit()