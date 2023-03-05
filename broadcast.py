import gmpy2
from functools import reduce
from Crypto.Util.number import long_to_bytes

e = 5
n = []
c = []
filenames = ['Frame3', 'Frame8', 'Frame12', 'Frame16', 'Frame20']
for i in filenames:
    f = open(i, 'r')
    data = f.read()
    nn = int(data[:256], 16)
    cc = int(data[512:], 16)
    n.append(nn)
    c.append(cc)


def CRT(mi, ai):
    M = reduce(lambda x, y: x * y, mi)
    ai_ti_Mi = [a * (M // m) * gmpy2.invert(M // m, m) for (m, a) in zip(mi, ai)]
    return reduce(lambda x, y: x + y, ai_ti_Mi) % M


m = CRT(n, c)
tmp = gmpy2.iroot(m, e)
tmp = hex(tmp[0])[2:]
number = int(tmp[16:24], 16)
plain = long_to_bytes(int(tmp[-16:], 16))
print(plain)
