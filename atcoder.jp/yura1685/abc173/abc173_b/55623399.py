N = int(input())
C0, C1, C2, C3 = 0, 0, 0, 0
for i in range(N):
    ans = input()
    if ans == 'AC':
        C0 += 1
    elif ans == 'WA':
        C1 += 1
    elif ans == 'TLE':
        C2 += 1
    elif ans == 'RE':
        C3 += 1
print('AC','x',C0)
print('WA','x',C1)
print('TLE','x',C2)
print('RE','x',C3)