from gmpy2 import invert, powmod, is_prime, gcd, next_prime
import binascii

n = []
e = []
c = []
ans = []


def Pollard_p_1(N):
    a = 2
    f = a
    while 1:
        for n in range(1, 200000):
            f = powmod(f, n, N)
            if is_prime(n):
                d = gcd(f - 1, N)
                if 1 < d < N:
                    return d
                elif d >= N:
                    f = next_prime(a)
                    break
        else:
            break


filenames = ['Frame2', 'Frame6', 'Frame19']
for i in filenames:
    f = open(i, 'r')
    data = f.read()
    n0, e0, c0 = int(data[:256], 16), int(data[256:512], 16), int(data[512:], 16)
    n.append(n0)
    e.append(e0)
    c.append(c0)

for i in range(len(n)):
    p = Pollard_p_1(n[i])
    q = n[i] // p
    phi_of_frame = (p - 1) * (q - 1)
    d = invert(e[i], phi_of_frame)
    m = powmod(c[i], d, n[i])
    ans.append(binascii.a2b_hex(hex(m)[-16:]))
for i in ans:
    print(i)
# My secret is a f\*\*\*\*\*\*\*\*\*\***************instein. That is "Logic will get********m A to B. Imagin********************************.
# My secret is a f************************instein. That is "Logic will get********m A to B. Imagin********************************.