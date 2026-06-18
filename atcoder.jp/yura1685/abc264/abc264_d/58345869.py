s = input()
ans = 0
c = s.index('a')
ans += c
s = 'a' + s[:c] + s[c+1:]
c = s.index('t')
ans += c-1
s = 'at' + s[1:c] + s[c+1:]
c = s.index('c')
ans += c-2
s = 'atc' + s[2:c] + s[c+1:]
c = s.index('o')
ans += c-3
s = 'atco' + s[3:c]+ s[c+1:]
c = s.index('d')
ans += c-4
s = 'atcod' + s[4:c] + s[c+1:]
print(ans + (s[-1]=='e'))