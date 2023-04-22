#time O(N) space O(1)
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0

    first = None
    second = None
    for ele in array:
        if first is None or second is None:
            if first is None:
                first = ele
            else:
                second = first
                first = max(second,ele)
        else:
            curr = max(first,second+ele)
            second = first
            first = curr
    return first
