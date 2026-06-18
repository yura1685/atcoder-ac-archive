N = int(input())
m = list(map(int,input().split()))

study = 0
for i in m:
    study += max(80-i, 0)
print(study)