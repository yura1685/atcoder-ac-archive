N = int(input())
w = list(map(str,input().split()))
takahashi = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun', 'TAKAHASHIKUN.', 'Takahashikun.', 'takahashikun.']

ans = 0
for i in w:
    if i in takahashi:
        ans += 1
print(ans)