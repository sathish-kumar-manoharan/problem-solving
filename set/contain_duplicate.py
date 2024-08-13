from typing import List
"""
https://leetcode.com/problems/contains-duplicate/
"""

def containsDuplicate1(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

def containsDuplicate(self, nums: List[int]) -> bool:
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    for key in count:
        if count[key] > 1:
            return True

    return False

"""

Time complexity: O(n). We do search() and insert() for n times and each operation takes constant time.

Space complexity: O(n). The space used by a hash table is linear with the number of elements in it.

"""
def contains_duplicate(list: List[int]) -> bool:
    seen = set()

    for num in list:
        if num in seen:
            return True
        seen.add(num)
    return False


print(contains_duplicate([1,4,652,12,4]))