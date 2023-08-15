def test(fn):
    cases = [(3, 5), (1.1, 21), (5, 6), (2, -4)]
    answers = [a ** b for (a, b) in cases]

    for i in range(len(cases)):
        assert round(fn(cases[i][0], cases[i][1])) == round(answers[i])

    print("All tests passed!")


def power_x_y(x, y):
    if y < 0:
        x, y = 1/x, -y
    res = 1
    while y:
        if y & 1:
            res *= x
        x *= x
        y >>= 1 
    return res

test(power_x_y)
