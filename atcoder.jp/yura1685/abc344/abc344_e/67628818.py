# -----------------------------------------------------------
# Insertとかそういう系は多分TLEになるので論外
# 配列 L を用意して，L[x] に，x の後ろにある数を入れる？
# 任意のクエリの後に A の要素は相異なることが保証されるので
# L[x] = z のとき，1 x y というクエリが来たら，
# L[x] = y, L[y] = z とすれば対応できる。
# 2 x で x の値を削除するとき，L[?] = x, L[x] = y 
# となる ? が存在するならば，L[?] = y にする必要があるので
# 各数字の前にある数字も新たな配列を用意して記録する必要がありそう
# なんか問題のオーダー見たら値がバカでかくて草
# だからdictで振り分けないといけないっぽい？
# 最後の出力にあたって、先頭の値は保持しておいたほうが良さそう。
# -----------------------------------------------------------

from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]

F = defaultdict(int)
B = defaultdict(int)
head = A[0]

for i in range(N-1):
    B[A[i]]   = A[i+1]
    F[A[i+1]] = A[i]

Q = int(input())
for _ in range(Q):
    q = [int(x) for x in input().split()]
    if q[0] == 1:
        x, y = q[1:]
        if B[x] == 0:
            B[x] = y
            F[y] = x
        else:
            z = B[x]
            B[x], B[y] = y, z
            F[y], F[z] = x, y
    else:
        x = q[1]
        if F[x] == 0:
            y = B[x]
            F[y], B[x] = 0, 0
            head = y
        else:
            y = F[x]
            if B[x] == 0:
                F[x], B[y] = 0, 0
            else:
                z = B[x]
                B[y] = z
                F[z] = y
                B[x], F[x] = 0, 0

now = head
while now:
    print(now)
    now = B[now]