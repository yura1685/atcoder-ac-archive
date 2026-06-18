from math import comb

N, P = map(int,input().split())
A = list(map(int,input().split()))
odd, even = [], []
for a in A:
    if a % 2 == 1:
        odd.append(a)
    else:
        even.append(a)

ans_even = 2**len(even)
ans_odd  = 0

if P == 0:
    for n in range(len(odd)):
        ans_odd += comb(len(odd), 2*n)

else:
    for n in range(len(odd)):
        ans_odd += comb(len(odd), 2*n+1)    

if P == 1 and ans_odd == 0:
    print(0)
else:
    print(ans_even if ans_odd==0 else ans_even*ans_odd)