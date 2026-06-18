N = int(input())
Name, Age = [], []
for i in range(N):
    S, A = map(str,input().split())
    Name.append(S)
    Age.append(int(A))

min_age = Age.index(min(Age))

L = Name[min_age:] + Name[:min_age]

print('\n'.join(L))