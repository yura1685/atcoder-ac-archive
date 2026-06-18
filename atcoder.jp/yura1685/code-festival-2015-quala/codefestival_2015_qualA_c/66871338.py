N, T = map(int,input().split())

taka = 0
copy = []
for _ in range(N):
    A, B = map(int,input().split())
    taka += A
    copy.append(A-B)
copy.sort(reverse=True)

if taka <= T:
    print(0)
    exit()

for i in range(N):
    taka -= copy[i]
    if taka <= T:
        print(i+1)
        exit()
print(-1)