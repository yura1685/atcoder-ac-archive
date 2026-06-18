H1, M1, H2, M2, K = map(int,input().split())
T1 = 60*H1 + M1
T2 = 60*H2 + M2
print(T2-K-T1)