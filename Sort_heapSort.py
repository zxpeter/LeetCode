# 算法流程：首先建立大顶堆，之后交换最后一个元素和第一个元素，再不断调整以root为根的堆
# 最优解法，两处地方省时间
# 1. 判断叶子节点是否存在，如果没有左，一定没有右
# 2. 开始建立堆时，从最后一个非叶子节点处开始建立，从后往前，免除叶子节点的判断时间

def adjust_heap(nums, n, root):
    if 2*root + 1 < n: # must have left before have right, save time!
        if 2*root + 2 < n and nums[2*root + 2] > nums[2*root + 1]:
            large = 2*root + 2
        else:
            large = 2*root + 1
        if nums[large] > nums[root]:
            nums[large], nums[root] = nums[root], nums[large]
            adjust_heap(nums, n, large) # adjust the sub tree which root is k, 开始从交换之后的叶子节点递归调整下面的子树

def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):  # start from non-leaf node, save time!
        adjust_heap(nums, n, i)   # what is inplace? finally know that nums[:n] is a new array!
    for i in range(n-1, 0, -1):   # only need to adjust root
        nums[i], nums[0] = nums[0], nums[i]
        adjust_heap(nums, i, 0)

if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap_sort(nums)
    # n = len(nums)
    print(nums)



