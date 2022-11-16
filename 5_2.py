##
## Plus One
##
from random import randint

def plus_one(A):
    '''
    Paremeters:
    A -- list(num, num, num, ...) -> list(num, num, num, ...)
    A is the encoding of an iteger, list of digits
    
    Returns:
    A list of digit encodings with one added to integer (encoded by A)

    Examples:
    >>> plus_one([1,2,9])
    >>> [1,3,0]
    
    >>> plus_one([9])
    >>> [1,0]

    >>> plus_one([1,2,7])
    >>> [1,2,8]
     
    '''
    A[-1] += 1
    # reverse range, i is not decreasing by on from len(A) to 1
    # Leave out 0 index for now, it will be precessed outside the loop
    for i in range(1, len(A))[::-1]:
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    ## Now process the first digit
    if A[0] == 10:
        A[0] = 0
        A.insert(0, 1)

    return A

#def test(num_test=10):
#    tests = []
#    answers = []
#    for _ in range(num_test):
#        r = randint(0, 10000) 
#        tests.append([int(i) for i in str(r)]) 
#        answers.append([int(i) for i in str(r + 1)])
    


