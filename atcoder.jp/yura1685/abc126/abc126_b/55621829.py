S = input()
if 1 <= int(S[2:]) <= 12:
    if 1 <= int(S[:2]) <= 12:
        print('AMBIGUOUS')
        
    else:
        print('YYMM')
else:
    if 1 <= int(S[:2]) <= 12:
        print('MMYY')
    else:
        print('NA')