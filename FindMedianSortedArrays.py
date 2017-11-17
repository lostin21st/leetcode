"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).
(有两个长度分别为m，n且排过序的数组.寻找这两个数组的中位数.时间复杂度不超过O(log(m+n)))
"""

def findMedianSortedArray(nums1,nums2):
    nums1.extend(nums2)
    //extend方法是将可迭代对象中的元素添加到尾部
    nums = sorted(nums1)
    if len(nums)%2 == 0:
        result = (nums[len(nums)//2]+nums[len(nums)//2-1])/2
    else:
        result = nums[len(nums)//2]
    return float(result)

