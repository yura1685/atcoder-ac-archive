A, B, C, D = map(int,input().split())
if 2*max(A,B,C,D) == A + B + C + D:
    print('Yes')
elif A+B==C+D or A+C==B+D or A+D==B+C:
    print('Yes')
else:
    print('No')