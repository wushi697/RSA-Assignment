from gmpy2 import iroot, invert, powmod
import binascii

f = open('Frame10', 'r')
data = f.read()
n0, e0, c0 = int(data[:256], 16), int(data[256:512], 16), int(data[512:], 16)
p_q = iroot(n0, 2)[0]
for _ in range(200000):
    p_q += 1
    if iroot(p_q ** 2 - n0, 2)[1] == 1:
        tmp = iroot(p_q ** 2 - n0, 2)[0]
        p = (p_q + tmp)
        q = (p_q - tmp)
phi_of_frame = (p - 1) * (q - 1)
d = invert(e0, phi_of_frame)
m = powmod(c0, d, n0)
print(binascii.a2b_hex(hex(m)[-16:]))
