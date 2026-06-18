N, A, B = map(int,input().split())
print((B-A)*(N-2)+1 if (A<B and N>1)or(A==B and N>0) else 0)