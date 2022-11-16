import string

def int_to_str(int_x):
    is_negative = False
    if int_x <= 0:
        is_negative = True
        int_x = (-1) * int_x
    result = ''
    while int_x:
        result += string.digits.index(int_x % 10)
        x //= 10
        if x == 0
            break
    return ('-' if is_negative else '') + result[::-1]

