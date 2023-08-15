import math 

def test(fn):
    cases = [1, 7, 11, 121, 12344321, -1, 23, -123321, 234, 14]
    answers = [True, True, True, True, True, False, False, False, False, False]

    for i in range(len(cases)):
        assert fn(cases[i]) == answers[i], fn(cases[i])
    
    print('All tests passed!')


# uses extra copy of number
# this solution shows that i can reverse digits of an int but is not better then comparing reversed string.
def polindrome(n):
    if n < 0:
        return False 
    # reverse and compare
    result = 0
    n_temp = n # is this a pointer or a copy?
    while n_temp:
        result = 10 * result + n_temp % 10 
        n_temp //= 10
    return (True if n == result else False)
    # dont forget to check signs


def polindrome_2(n):
    if n < 0:
        return False
    n_digits = math.floor(math.log(n, 10)) + 1# why + 1?  
    while math.floor((n_digits) / 2)!= 0:
        lsb = n % 10
        msb = (n // (10 ** (n_digits - 1))) % 10
        if lsb != msb:
            return False
        n_digits -= 2 # annoying detail: dont forget that we also do 10 // 10, so we need to compensate for that and shift 2 digits here
        n //= 10
    return True


test(polindrome)
test(polindrome_2) 
