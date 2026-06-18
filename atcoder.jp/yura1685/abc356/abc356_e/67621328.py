# ----------------------------------------------
# 対称性があるから昇順ソートしていい
# すると，floor(max(Ai,Aj)/min(Ai,Aj)) = floor(Aj/Ai) となる
# たとえばAiに対してfloor(Aj/Ai) = k となる個数をそれぞれ調べても良さそう
# 最初にiのループ回してそのあとkのループを回すと多分計算量がアウト
# floor(Aj/Ai) = k となる Aj の個数は，
# (floor(Aj/Ai) <= k となる個数) - (floor(Aj/Ai) <= k-1 となる個数)
# だから先に累積和で x に対し Aj <= x となる個数を記録(Y_xとする)しておけば，
# 上の式の値はY_{Ai*(k+1)} - Y_{Ai*k} に等しい
# これだと同じ数字に対して複数のカウントをするので，それを除外してあげる
# ----------------------------------------------

from more_itertools import run_length
from itertools import accumulate

N = int(input())
A = [int(a) for a in input().split()]
A.sort()
B = list(run_length.encode(A))
C = [0]*(A[-1]+1)
for num, cnt in B:
    C[num] = cnt
C = list(accumulate(C))

ans = 0
for i in range(len(B)):
    num, cnt = B[i]
    for k in range(1,A[-1]//num+1):
        ans += (C[min(num*(k+1),A[-1]+1)-1] - C[num*k-1])*cnt*k

for _, cnt in B:
    ans -= cnt*(cnt+1)//2

print(ans)