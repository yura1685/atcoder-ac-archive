N = int(input())
T = input()
if N == 1:
    if T == '0':
        print(10**10)
    else:
        print(2*10**10)
    exit()

if T[0] == '0':
    T = '11' + T
    N += 2
elif T[1] == '0':
    T = '1' + T
    N += 1

if T[-1] == T[-2] == '1':
    T += '0'
    N += 1
if T[-1] == '1' and T[-2] == '0':
    T += '10'
    N += 2

if N % 3 != 0 or T.count('110') != N // 3:
    exit(print(0))

print(10**10 - N//3 + 1)