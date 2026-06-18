I, O, _, J, L, _, _ = map(int, input().split())
I2, J2, L2 = I, J, L

K1 = 0
if I and J and L:
    K1 = 6
    I, J, L = I-1, J-1, L-1
    K1 += I // 2 * 4 + J // 2 * 4 + L // 2 * 4

K2 = I2 // 2 * 4 + J2 // 2 * 4 + L2 // 2 * 4
print((max(K1, K2) + O * 2) // 2)