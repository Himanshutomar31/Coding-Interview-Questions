import sys

# time O(nlogn + mlogm), space O(n or m)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    n1 = len(arrayOne)
    n2 = len(arrayTwo)
    i = 0
    j = 0
    res = sys.maxsize
    values = []
    while i < n1 and j < n2:
        if arrayOne[i] <= arrayTwo[j]:
            temp = abs(arrayTwo[j] - arrayOne[i])
            if res > temp:
                res = temp
                values.append([arrayOne[i], arrayTwo[j]])
            i += 1
        else:
            temp = abs(arrayTwo[j] - arrayOne[i])
            if res > temp:
                res = temp
                values.append([arrayOne[i], arrayTwo[j]]) 
            j += 1
    return values[-1]
            
