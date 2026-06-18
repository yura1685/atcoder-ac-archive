N = int(input())
S = input()
p = (N+1)//2 - 1
if S[p] == '/':
    if S[:p] == '1'*p:
        if S[p+1:] == '2'*p:
            print('Yes')
            exit()
print('No')