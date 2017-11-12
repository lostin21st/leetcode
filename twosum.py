"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
    Given nums = [2,7,11,15] target = 9,
    Because nums[0] + num[1] = 2+7 = 9,
    return [0,1]
"""

def twoSum(nums, target):
    """
    逐个遍历相加，和为target时返回
    """
    for i,x in enumerate(nums):
        for j in range(i+1, len(nums)):
            if x+nums[j] == target:
                return [i,j]

print(twoSum([2,7,11,15],9))
