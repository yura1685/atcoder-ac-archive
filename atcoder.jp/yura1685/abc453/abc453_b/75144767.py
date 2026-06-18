T, X = map(int, input().split())
now, *A = map(int, input().split())
print(0, now)
for i, a in enumerate(A):
    if abs(now - a) >= X:
        print(i+1, a)
        now = a