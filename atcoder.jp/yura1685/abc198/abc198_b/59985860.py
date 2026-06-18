N = list(input())
if N == ['0']:
    print('Yes')
    exit()
while N[-1] == '0':
    N.pop(-1)
c = []
for i in range(len(N)):
    c.append(N[-i-1])
print('Yes' if c == N else 'No')