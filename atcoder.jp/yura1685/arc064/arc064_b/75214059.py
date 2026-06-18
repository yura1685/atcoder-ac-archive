s = input()
b1 = (s[0] == s[-1])
b2 = (len(s) % 2 == 1)
print('First' if b1 ^ b2 else 'Second')