A, B, K = map(int,input().split())
for i in range(K):
    if i % 2 == 0:
        #高橋のターン
        if A % 2 == 1:
            A -= 1
        B += A//2
        A //= 2
    else:
        #青木のターン
        if B % 2 == 1:
            B -= 1
        A += B//2
        B //= 2
print(A,B)