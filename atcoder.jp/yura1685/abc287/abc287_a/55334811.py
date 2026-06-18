N = int(input())
Agree = 0
for i in range(N):
    if input() == 'For':
        Agree += 1
if Agree > N - Agree:
    print('Yes')
else:
    print('No')