#time O(N^2), space 0(1) 
def two_number_sum(array, target_sum):
    for i in range(len(array)-1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []
