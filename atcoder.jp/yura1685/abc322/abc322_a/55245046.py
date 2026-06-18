N = int(input())
S = input()
for i in range(N -2):
    if S [i] == 'A':
        if S[i+1] == 'B':
            if S[i+2] == 'C':
                print(i+1)
                exit()
print(-1) 