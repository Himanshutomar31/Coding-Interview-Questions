#O(n) time
def isMonotonic(array):
    n = len(array)
    if n == 0 or n == 1:
        return True

    check_inc = False
    check_dec = False

    if array[0] > array[1]:
        check_dec = True 

    if array[0] < array[1]:
        check_inc = True

    if check_dec is False and check_inc is False:
        if array[-2] > array[-1]:
            check_dec = True 
        if array[-2] < array[-1]:
            check_inc = True       
        

    for i in range(1, n):
        if check_inc:
            if array[i-1] > array[i]:
                return False 
        if check_dec:
            if array[i-1] < array[i]:
                return False
    return True
    
    
