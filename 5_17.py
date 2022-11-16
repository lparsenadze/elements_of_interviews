##
## Check Valid Sudoku layout
##
import numpy as np


def check_sudoku(A):
    ## for LeetCode problem 36
    ## input is list of str
    ## for leetcode use below 2 lines to convert to array
    
    # numerical_board = [[0 if i=="." else int(i) for i in l] for l in board]
    # A = np.array(numerical_board)

    def valid_list(l):
        c = {i: 0 for i in range(1, 10)}
        c[0] = -9**2  #-1e9 <- slower speed performance
        for i in l:
            c[i] += 1
            if c[i] > 1:
                return False
        return True
    for i in range(9):
        if not (valid_list(list(A[i])) and valid_list(list(A.T[i]))):
            return False
    for i in range(3):
        for j in range(3):
           if not(valid_list(list(A[i*3:i*3+3, j*3:j*3+3].reshape(9,)))):
               return False
    
    return True
