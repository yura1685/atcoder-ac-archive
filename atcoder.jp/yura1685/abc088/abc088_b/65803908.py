N = int(input())
a = list(map(int,input().split()))
a.sort()
Alice, Bob = 0, 0
for _ in range(N//2):
    Alice += a.pop()
    Bob += a.pop()
if a != []:
    Alice += a[0]
print(Alice-Bob)