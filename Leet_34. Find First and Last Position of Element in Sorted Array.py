34. Find First and Last Position of Element in Sorted Array
# 二分查找，记住mid+1
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_ = len(nums)
        l = 0
        r = len_
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res_l = mid
                while res_l >= 0 and nums[res_l] == target:
                    res_l -= 1
                res_r = mid
                while res_r < len_ and nums[res_r] == target:
                    res_r += 1
                return [res_l+1,res_r-1]
            
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        return [-1,-1]
