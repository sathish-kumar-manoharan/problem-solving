
def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    lookup = {}
    
    for index, number in enumerate(numbers):
        lookup[number] = index
        
    for index, number in enumerate(numbers):
        complement = target - number
        
        if complement in lookup and lookup[complement] != index:
            return [index, lookup[complement]]
            
    return []

print(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))