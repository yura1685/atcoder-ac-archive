N = int(input())
S = input()

ans = S.count('R')*S.count('G')*S.count('B')

for i in range(N-2):
    for j in range(i+1,N-1):
        k = 2*j - i
        if k >= N:
            break
        if {S[i],S[j],S[k]} == {'R','G','B'}:
            ans -= 1

print(ans)