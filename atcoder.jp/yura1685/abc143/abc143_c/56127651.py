N = int(input())
S = input()

slimes = 1
check = 0

while check != N-1:
    if S[check] != S[check+1]:
        slimes += 1
    check += 1

print(slimes)