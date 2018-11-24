11. Container With Most Water
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

If height[L] < height[R], move L, else move R. Say height[0] < height[5], area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, res, width = 0, len(height)-1, 0, len(height)-1
        for i in range(width, 0, -1):
            if height[left] < height[right]:
                res = max(res, i*height[left])
                left += 1
            else:
                res = max(res, i*height[right])
                right -= 1
        return res

#         max_contain = 0
#         max_former = 0
#         print(len(height))
#         count = 0
#         for i in range(len(height)):
#             if i == 0 or height[i] > height[max_former]:
#                 count += 1
#                 for j in range(i, len(height)):
#                     max_contain = max(max_contain, (j-i)*min(height[i], height[j]))
#             max_former = max(max_former, i)
            
#         print(count)
#         return max_contain        
    
