N = int(input())
people = list(map(int,input().split()))
query = int(input())
for _ in range(query):
    A, B = map(int,input().split())
    A_num = people.index(A)
    B_num = people.index(B)
    print(A if A_num < B_num else B)