# O(N) time and O(1) space
def isValidSubsequence(array, sequence):
    n1 = len(sequence)
    n2 = len(array)
    if n1 > n2:
        return False

    index1 = 0
    index2 = 0
    while index1 < n1 and index2 < n2:
        if sequence[index1] == array[index2]:
            index1 += 1
        index2 += 1
        
    return index1 == n1
