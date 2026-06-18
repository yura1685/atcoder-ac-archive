N = int(input())
F = [int(''.join(input().split()),2) for _ in range(N)]
P = [tuple(map(int,input().split())) for _ in range(N)]

ans = -168516851685
for bits in range(1,1 << 10):
    prof = 0
    for i in range(N):
        n = bits & F[i]
        prof += P[i][n.bit_count()]
    ans = max(ans, prof)

print(ans)