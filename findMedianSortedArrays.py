class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        k = len_1 + len_2
        if k % 2 == 0:# even
            return (self.findKth(nums1, nums2, 0, len_1, 0, len_2, int(k/2)) +
                    self.findKth(nums1, nums2, 0, len_1, 0, len_2, int(k/2) + 1)) / 2

        else: # odd
            return self.findKth(nums1, nums2, 0, len_1, 0, len_2, int(k//2) + 1)

    def findKth(self, nums1, nums2, start1, len1, start2, len2, k):
        if len1 > len2:
            return self.findKth(nums2, nums1, start2, len2, start1, len1, k)

        if len1 == 0: #在某一步搜索中子数组的长度为0了，这表示有一个数组中的元素完全被抛弃掉，此时另外一个子数组的第k个元素就是我们要求的第k小的元素
            return nums2[start2 + k - 1]

        if k == 1: # finding 1st smallest element
            return min(nums1[start1], nums2[start2])

        p = min(max(k // 2, 1), len1) # p不能为0，否则在nums1中等于是没有做“前进”的动作，这是不允许的
        q = k - p
        if (nums1[start1 + p - 1] == nums2[start2 + q - 1]):
            return nums1[start1 + p - 1]
        elif (nums1[start1 + p - 1] > nums2[start2 + q - 1]):
            return self.findKth(nums1, nums2, start1, len1, start2+q, len2-q, k-q)
        elif (nums1[start1 + p - 1] < nums2[start2 + q - 1]):
            return self.findKth(nums1, nums2, start1+p, len1-p, start2, len2, k-p)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1]
    nums2 = [2,3,4,5,6]
    median = solution.findMedianSortedArrays(nums1, nums2)
    print(median)

