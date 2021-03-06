class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, other):
        gcd = lambda x, y: x if y == 0 else gcd(y, x%y)
        lcm = self.denominator / gcd(self.denominator, other.denominator) * other.denominator
        tmp_numerator = lcm / self.denominator * self.numerator + lcm / other.denominator * other.numerator
        co = gcd(tmp_numerator, lcm)
        tmp_numerator = tmp_numerator / co
        tmp_denominator = lcm / co
        return Fraction(tmp_numerator, tmp_denominator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return '%d/%d' % (self.numerator, self.denominator)


n = int(raw_input())
fracs = []
for num in raw_input().split():
    numerator, denominator = map(int, num.split('/'))
    fracs.append(Fraction(numerator, denominator*n))
print reduce(lambda x, y: x+y, fracs)