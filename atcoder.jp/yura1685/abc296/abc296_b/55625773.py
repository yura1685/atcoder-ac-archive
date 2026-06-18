line = 0
for i in range(8):
    line += 1
    S = input()
    if S != '........':
        a = str(9-line)
        for i in range(8):
            if S[i] == '*':
                alp = ['a','b','c','d','e','f','g','h'][i]
                print(alp + a)
                exit()