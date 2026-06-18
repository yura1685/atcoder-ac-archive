def sinwa(N):
    if N == 2:
        return ['()']
    ans = set()
    for x in sinwa(N-2):
        ans.add('('+x+')') 
    for i in range(1,N//2):
        A, B = sinwa(2*i), sinwa(N-2*i)
        for a in A:
            for b in B:
                ans.add(a+b)
                ans.add(b+a)
    return sorted(list(ans))

N = int(input())
if N % 2 == 0:
    for xxx in sinwa(N):
        print(xxx)