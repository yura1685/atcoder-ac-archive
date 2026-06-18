N = int(input())
A = sorted(int(input()) for _ in range(N))
B = list(reversed(A))

if N % 2:
    a = -2*sum(A[:N//2-1]) - A[N//2-1] - A[N//2] + 2*sum(A[N//2+1:])
    b = -2*sum(B[:N//2-1]) - B[N//2-1] - B[N//2] + 2*sum(B[N//2+1:])
    print(max(a, abs(b)))

else:
    a = -2*sum(A[:N//2-1]) - A[N//2-1] + A[N//2] + 2*sum(A[N//2+1:])
    b = -2*sum(B[:N//2-1]) - B[N//2-1] + B[N//2] + 2*sum(B[N//2+1:])
    print(max(a, abs(b)))