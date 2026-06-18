N = int(input()) - 1
ans = ['4'] * 10
for i in range(10):
    if N >> i & 1:
        ans[-1-i] = '7'
print(''.join(ans))