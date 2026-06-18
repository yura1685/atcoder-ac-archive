S = input()
T = input()
c = '0ABCDE'
s = (c.index(S[0])-c.index(S[1])) % 5
t = (c.index(T[0])-c.index(T[1])) % 5
collect = [{1,1},{2,2},{3,3},{4,4},{1,4},{2,3}]
print('Yes' if {s,t} in collect else 'No')