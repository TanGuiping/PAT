a, b = raw_input().split()
a1, b1 = map(int, a.split('/'))
a2, b2 = map(int, b.split('/'))
gcd = lambda x, y: x if y == 0 else gcd(y, x % y)
lcm = b1 / gcd(b1, b2) * b2
a = a1*lcm/b1+a2*lcm/b2
co = gcd(a , lcm)
if lcm / co != 1:
    print '%d/%d' % (a/co, lcm/co)
else:
    print a/co



