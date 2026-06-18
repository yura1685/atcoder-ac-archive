S = input()

hoge = ''
for s in S:
    if s in 'ACGT':
        hoge += 'X'
    else:
        hoge += 'O'
        
print(len(max(map(str,hoge.split('O')))))