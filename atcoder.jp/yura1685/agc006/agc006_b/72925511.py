N, x = map(int,input().split())
if x == 1 or x == 2*N-1: exit(print('No'))
A = list(range(1,2*N))
shift = (x - N) % (2*N-1)
B = A[shift:] + A[:shift]
print('Yes')
for b in B: print(b)