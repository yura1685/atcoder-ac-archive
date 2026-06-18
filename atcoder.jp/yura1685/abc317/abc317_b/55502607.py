N = int(input())
A = list(map(int,input().split()))
start, end = min(A), max(A)
for i in range(start,end+1):
    if i not in A:
        print(i)
        exit()