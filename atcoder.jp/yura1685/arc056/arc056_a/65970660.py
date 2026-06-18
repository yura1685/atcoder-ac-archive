A, B, K, L = map(int,input().split())

pay = 0

m = K // L
pay += m*B
K -= m*L
pay += min(B, A*K)
print(pay)