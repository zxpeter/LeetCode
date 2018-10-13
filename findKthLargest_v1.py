
    # 最大堆是要建立长度为k的然后依次往里添加，，还是建立长度为n的，然后取出最大的k个。
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

    def findKthLargest(self, nums, k): # AC, 好像比上面的解法更快，反正partition是没有错的
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthLargest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthLargest(nums[:pos], k)
            else:
                return nums[pos]

class Solution:
    def findKthLargest(self, nums, k):        
        return heapq.nlargest(k, nums)[-1]
    
    
    class Solution:
    def findKthLargest(self, nums, k): # 小顶堆，全部压进去，最后弹出n-k个，剩下的堆顶就是第k大的数
        heap = []                      # 对于大数据，首先压入k个数，比较堆顶和下一个数的大小，比堆顶小则进入堆
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
