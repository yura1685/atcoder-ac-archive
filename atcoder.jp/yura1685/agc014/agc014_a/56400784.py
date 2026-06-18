A, B, C = map(int,input().split())
a, b, c = A, B, C

ans = 0
while True:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        print(ans)
        exit()
    ans += 1
    A, B, C = (B+C)//2, (C+A)//2, (A+B)//2
    if A == a and B == b:
        print(-1)
        exit()