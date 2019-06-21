def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) ==1:
        return x*y
    m = max(len(str(x)), len(str(x)))
    m2 = m//2
    a = x//10**m2
    b = x%10**m2
    c = y//10**m2
    d = y%10**m2
    AC = karatsuba(a, c)
    BD = karatsuba(b, d)
    ADBC = karatsuba(a+b, c+d) - AC - BD
    return (AC* 10**(2*m2)) + ((ADBC) * 10**(m2)) + BD


answer = karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
correct_result = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
print(answer == correct_result)
