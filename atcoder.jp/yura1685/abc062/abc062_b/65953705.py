H, W = map(int,input().split())
glid = ['#'+input()+'#' for _ in range(H)]
glid = ['#'*(W+2)] + glid + ['#'*(W+2)]
for row in glid:
    print(''.join(row))