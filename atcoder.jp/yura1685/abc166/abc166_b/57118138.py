n, k = map(int,input().split())
have = [0]*n
for i in range(k):
    candy = int(input())
    sunuke = list(map(int,input().split()))
    for k in sunuke:
        have[k-1] = 1
print(have.count(0))