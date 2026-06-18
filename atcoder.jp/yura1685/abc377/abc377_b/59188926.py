c = [0]*8
x, y = 0, 0

for i in range(8):
  S = input()
  if S == '........':
    x += 1
  c[i] = S
  
for i in range(8):
  if c[0][i] == '.' and c[1][i] == '.' and c[2][i] == '.' and c[3][i] == '.' and c[4][i] == '.' and c[5][i] == '.' and c[6][i] == '.' and c[7][i] == '.':
    y += 1
    
print(x*y)