a, op, b = raw_input().split()
if op not in ('+', '-', '*', '/', '%'):
    print 'ERROR'
else:
    print int(float(a)/float(b)) if op == '/' else eval(a+op+b)
