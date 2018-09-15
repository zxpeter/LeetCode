class Solution:

    def partition(self, nums, l, r):
        last = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] >= last:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[r], nums[i+1] = nums[i+1], nums[r]
        return i+1

    def findKthLargest(self, nums, k):
        """11
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 0
        r = len(nums)-1
        if k > r+1:
            return
        mid = self.partition(nums, l, r)
        while mid != k-1:
            if mid < k-1:
                mid = self.partition(nums, mid + 1, r)
            else:
                mid = self.partition(nums, l, mid-1)

        return nums[mid]

if __name__ == '__main__':
    soul = Solution()
    nums = [2,1]
    k = 2
    res = soul.findKthLargest(nums, k)
    print(res)
    print(nums)
