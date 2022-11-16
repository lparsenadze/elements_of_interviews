##

import string

def change_base(num, b1, b2):
    def to_decemal(num, b):
        res = string.digits.index(num[-1])
        for i in range(1, len(num)):
            res += string.digits.index(num[~i])*b**i
        return res
    def to_other(num, b):
        res = []
        while True:
            rem = num % b
            num = num // b
            res.append(rem)
            if num == 0:
                break 
        return res[::-1]
    mapping = dict(zip([10,11,12,13,14,15,16], "ABCDEFG"))
    is_negative = False
    if num[-1] == '-':
        is_negative = True
        num = num[1:]
    dec = to_decemal(num, b1)
    other = to_other(dec, b2)
    if is_negative:
        return '-' + ''.join([mapping(i) if i in mapping else chr(ord('0') + i) for i in other])
    return ''.join([mapping[i] if i in mapping else chr(ord('0') + i) for i in other])

## test example
## >>> change_base('615', 7, 13)
## >>> '1A7'
