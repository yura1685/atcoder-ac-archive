N = int(input())
A = list(map(int,input().split()))

S = sum(A)/2
s = 0
cnt = 0
gosa = float('inf')
while True:
    s += A[cnt]
    cnt += 1
    hoge = abs(S-s)
    if hoge > gosa:
        break
    gosa = hoge

print(int(2*gosa))