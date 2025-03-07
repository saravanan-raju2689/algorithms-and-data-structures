def subarray_with_zero_sum(arr):
    sum_set = set()
    current_sum = 0
    
    for num in arr:
        current_sum += num
        
        if current_sum == 0 or current_sum in sum_set:
            return True
        
        sum_set.add(current_sum)
    
    return False