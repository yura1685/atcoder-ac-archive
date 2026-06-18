N = int(input())

ans = []
while N:
    if N%2: r = 1
    else:   r = 0
    q = (r-N)//2
    ans.append(str(r))
    N = q

if not ans: ans = ['0']

print(''.join(ans[::-1]))