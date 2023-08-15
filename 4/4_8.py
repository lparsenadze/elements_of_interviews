def test(fn):
    cases = [234, 123, 56, 78, -56, -367, -8]
    answers = [432, 321, 65, 87, -65, -763, -8]

    for i in range(len(cases)):
        print(cases[i])
        assert fn(cases[i]) == answers[i], fn(cases[i])

    print('All tests passed!')


def reverse_digits(n):
    is_neg = False
    if n < 0:
        is_neg = True
        n *= -1
    result = 0
    while n:
        last_digit = n % 10
        n //= 10
        result = result * 10 + last_digit
    return (-1 * result if is_neg else result)

test(reverse_digits) 
