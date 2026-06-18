S = input()
cnta, cntb, cntc = 0, 0, 0

for s in S:
    if s == 'A':
        cnta += 1
    if s == 'B':
        if cnta > 0:
            cntb += 1
            cnta -= 1
    if s == 'C':
        if cntb > 0:
            cntc += 1
            cntb -= 1

print(cntc)