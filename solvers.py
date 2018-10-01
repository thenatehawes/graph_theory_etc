

def ef_plus(a, b):
    x = a + b
    a_prime = x - b
    b_prime = x - a
    y = (a - a_prime) + (b - b_prime)

    return (x, y)

def c_ef_plus(a, b):
    (s1, e1) = ef_plus(a.real, b.real)
    (s2, e2) = ef_plus(a.imag, b.imag)
    
    s = s1 + 1j*s2
    e = e1 + 1j*e2

    return (s, e)

def ef_split(a):
    s = 27  # constant for double precision

    factor = (2**s + 1)

    c = factor * a
    x = c - (c - a)
    y = a - x

    return (x, y)


def ef_product(a, b):
    x = a * b

    (a1, a2) = ef_split(a)
    (b1, b2) = ef_split(b)
    y = a2 * b2 - (((x - a1*b1) - a2*b1) - a1*b2)

    return (x, y)


def c_ef_product(x, y):
    (a1, a2) = ef_split(x.real)
    (b1, b2) = ef_split(x.imag)
    (c1, c2) = ef_split(y.real)
    (d1, d2) = ef_split(y.imag)

    z1 = x.real * y.real
    z2 = x.imag * y.imag
    z3 = x.real * y.imag
    z4 = x.imag * y.real

    h1 = a2*c2 - (((x - a1*c1) - a2*c1) - a1*c2)
    h2 = b2*d2 - (((x - b1*d1) - b2*d1) - b1*d2)
    h3 = a2*d2 - (((x - a1*d1) - a2*d1) - a1*d2)
    h4 = b2*c2 - (((x - b1*c1) - b2*c1) - b1*c2)

    (z5, h5) = ef_plus(z1, -z2)
    (z6, h6) = ef_plus(z3, z4)
    p = z5 + 1j*z6
    e = h1 + 1j*h3
    f = -h2 + 1j*h4
    g = h5 + 1j*h6

    return (p, e, f, g)
