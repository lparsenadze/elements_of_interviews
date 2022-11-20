# Exercises from https://www.learnpython.org/en/Generators
## my solutions

def fib():
    #this is a null statement which does nothing when executed, useful as a placeholder.
    prev, curr = 1, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
