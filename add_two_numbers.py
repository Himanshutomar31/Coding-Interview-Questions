#time O(N^2), space 0(1) 
def two_number_sum(array, target_sum):
    for i in range(len(array)-1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []

#time O(N), space 0(N)
def two_number_sum(array, target_sum):
    complement_set = set()
    for num in array:
        complement = target_sum - num
        if complement in complement_set:
            return [complement, num]
        complement_set.add(num)
    return []

#time O(NlogN), space 0(1)
def two_number_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return []
