N = int(input())
S = input()
error = 0

for i in range(N):
    if error == 0 and S[i] == '*':
        print('out')
        exit()
    elif error == 0 and S[i] == '|':
        error += 1
    elif error == 1 and S[i] == '*':
        print('in')
        exit()
    elif error == 1 and S[i] == '|':
        print('out')
        exit()