def test_fn():
    exs = [10, 3, 5, 4, 11, 13]
    ans = [0, 0, 0, 1, 1, 1]
    for i in range(len(exs)):
        assert compute_parity_1(exs[i]) == ans[i], f'Expected: {ans[i], returned: {compute_parity(exs[i])}}'
    print('All tests passed for solution 1!')
    for i in range(len(exs)):
        assert compute_parity_2(exs[i]) == ans[i], f'Expected: {ans[i], returned: {compute_parity(exs[i])}}'
    print('All tests passed for solution 2!')


def compute_parity_1(bint):
    starting_bit = 0
    while bint:
        last_bit = bint & 1
        starting_bit ^= last_bit
        bint >>=  1
    return starting_bit


def compute_parity_2(x):
    result = 0
    while x: 
        #result ^= 1 # does the order in which we apply counter metter? TODO: Check in the debugger
        x &= x-1
        result ^= 1 
    return result


test_fn()
