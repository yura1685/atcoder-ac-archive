N = int(input())
S = input()
list = []
for i in range(N):
    list.append(S[i])
for i in range(N):
    if list[i] == 'M':
        list[i] = 1
    else:
        list[i] = 0
for i in range(N-1):
    if abs(list[i]-list[i+1]) != 1:
        print('No')
        exit()
print('Yes')