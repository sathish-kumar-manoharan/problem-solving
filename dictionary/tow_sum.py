
'''
input: nums = [2,7,11,15], target = 9
Output: [0,1]

'''

from typing import List

def two_sum(list, target):
    for num in list:
        if list.index(target - num):
            return [list.index(target-num), list.index(num)]

nums = [2,7,11,15]
target = 9

output = two_sum(nums, target)

print(output[0], output[1])

def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup = {}

    for index, value in enumerate(nums):
        compliment = target - value

        if compliment in lookup:
            return [lookup[compliment], index]

        lookup[value] = index