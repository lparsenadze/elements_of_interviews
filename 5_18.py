## Sol. by NeetCode
## with my minor modifications



def get_spiral(a):
    '''
    Problem: Return the spiral ordering of the 2D array.
    a - (m, n)
    '''        

    def in_bounds(left, right, top, bottom):
        '''
        Check if pointers are in bounds
        '''
        
        if not (left < right and top < bottom):
            return False
        return True
    
    res = []
    left, right = 0, len(a[0])
    top, bottom = 0, len(a)
    while in_bounds(left, right, top, bottom):
        # add all i in 1st row
        for i in range(left, right):
            res.append(a[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(a[i][right - 1])
        right -= 1
        if not in_bounds(left, right, top, bottom):
            break
        for i in range(right-1, left - 1, -1):
            res.append(a[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            res.append(a[i][left])
        left += 1
    return res
