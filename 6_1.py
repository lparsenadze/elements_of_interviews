import string

## insteas if impoerting string module we couls just use "012345689" (this is string.digits)

def int_ro_srt(x):
    is_negative = False
    if x < 0:
        x = -1 * x
        is_negative = True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    if is_negative:
        return '-' + ''.join(s[::-1])
    return ''.join(s[::-1])

def str_to_int(x):
    is_negative = False
    if x[0] == '-':
        is_negative = True
        x = x[1:]
    res = string.digits.index(x[-1])
    if len(x) == 1:
        return res
    j = 1
    for i in range(len(x) - 1)[::-1]:
        res += 10**j * string.digits.index(x[i])
        j += 1
    if is_negative:
        return -1 * res
    return res
