N = int(input())
A = list(map(int,input().split()))
Odd = 1
for p in A:
    if p % 2 == 0:
        Odd *= 2
print(3**N - Odd)