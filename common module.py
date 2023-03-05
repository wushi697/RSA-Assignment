from gmpy2 import invert, powmod
import binascii

f = open('Frame0', 'r')
data = f.read()
n0, e0, c0 = int(data[:256], 16), int(data[256:512], 16), int(data[512:], 16)
f = open('Frame4', 'r')
data = f.read()
n4, e4, c4 = int(data[:256], 16), int(data[256:512], 16), int(data[512:], 16)


def common_module_attack(N, e1, e2, c1, c2):
    d1 = invert(e1, e2)
    d2 = (d1 * e1 - 1) // e2
    true_c2 = invert(c2, N)
    return (powmod(c1, d1, N) * powmod(true_c2, d2, N)) % N


if n0 == n4:
    ans = common_module_attack(n0, e0, e4, c0, c4)
    answer = binascii.a2b_hex(hex(ans)[2:])
    print(answer[-8:])
