N, M = map(int,input().split())
name = input()
kit = input()

A = [name.count(chr(ord('A')+i)) for i in range(26)]
B = [ kit.count(chr(ord('A')+i)) for i in range(26)]

ans = 0
for i in range(26):
    if A[i] >= 1:
        if B[i] == 0:
            print(-1)
            exit()
        hoge = (A[i]+B[i]-1)//B[i]
        ans = max(ans,hoge)

print(ans)