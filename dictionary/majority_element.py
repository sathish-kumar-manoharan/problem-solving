import collections

# T:O(N^2)
# S:O(1)
def majority_element1(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int32
    """
    max_value = 0
    max_occurance = 0
    
    for number in nums:
        count = nums.count(number)
        
        if max_occurance < count:
            max_occurance = count
            max_value = number

    return max_value

# T:O(N)
# S:O(N)
def majority_element2(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int32
    """
    count = collections.Counter(nums)
    print("The majority of the element is ", max(count.keys(), key = count.get))

    print(count)

    for key, value in count.items():
        print("The key is ", key, " and the value is ", value)


# T:O(N)
# S:O(1)
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count += 1
        else:
            count += -1
        
        print("The value of num is ", num)
        print("The value of count is ", count)
        print("The value of candidate is ", candidate)

    return candidate

print(majority_element2([3,5,2,2,2,4,2,4]))

