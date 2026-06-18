s = set(input())
d = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
u = sorted(list(d - s))
print('None' if len(u) == 0 else u.pop(0))