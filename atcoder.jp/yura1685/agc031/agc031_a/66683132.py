N = int(input())
S = input()

ans = 1
for i in range(26):
    ans *= S.count(chr(i+ord('a')))+1

print((ans-1)%(10**9+7))