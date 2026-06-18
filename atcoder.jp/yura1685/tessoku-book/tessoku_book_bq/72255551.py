from atcoder.maxflow import MFGraph

N = int(input())
mf = MFGraph(2*N+2)

for i in range(1,N+1):
    C = input()
    mf.add_edge(0,i,1)
    mf.add_edge(i+N,2*N+1,1)
    for j in range(1,N+1):
        if C[j-1] == '.':
            continue
        mf.add_edge(i,j+N,1)

print(mf.flow(0,2*N+1))