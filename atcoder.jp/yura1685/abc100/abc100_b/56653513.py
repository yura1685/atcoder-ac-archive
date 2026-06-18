D, N = map(str,input().split())
print(N + '00'*int(D) if N != '100' else '101' + '00'*int(D))