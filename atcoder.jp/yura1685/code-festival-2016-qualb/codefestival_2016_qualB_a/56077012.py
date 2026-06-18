S = input()
T = 'CODEFESTIVAL2016'
diff = 0
for i in range(16):
    if S[i] != T[i]:
        diff += 1
print(diff)