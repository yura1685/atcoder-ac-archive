N = int(input())
S = input()
Q = int(input())

alp = [chr(97+i) for i in range(26)]
for _ in range(Q):
    c, d = map(str,input().split())
    for i in range(26):
        if alp[i] == c:
            alp[i] = d

ans = ''
for s in S:
    ans += alp[ord(s)-97]

print(ans)