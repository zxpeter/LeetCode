
# 暴力解法
def twoSum(self, nums, target):
        if not nums:
            return []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# 使用字典，不过建立字典过程需要全部遍历一遍数组，其实没有必要，
# 如方法3即可，一边简历，一边遍历，因为只有一组解
def twoSum(self, nums, target):
        if not nums:
            return []
        dict = {}
        for i in range(len(nums)):
            dict[target-nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in dict:
                if j != dict[nums[j]]:  # 去除 6=3+3 的情况
                    return [dict[nums[j]], j]

def twoSum(self, nums, target):
        if not nums:
            return []
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i

                
Two Sum II - Input array is sorted

# 之前的算法还是可以用
# 想到了头尾指针移动的算法，是最优的
def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
                
                
 # 看了discuss里的二分法，也并没有快
def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = (l + r)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
                
                
560. Subarray Sum Equals K
#  直接暴力，果断GG，TLE
class Solution:
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            j = i
            while j < len(nums):
                sum_ = sum(nums[i:j+1])
                print(sum_)
                if sum_ <= k:
                    if sum_ == k:
                        count += 1
                j += 1
        return count


    def subarraySum(self, nums, k):
        res = 0
        for i in range(len(nums)):
            prefixSum = 0
            for j in range(i, len(nums)):
                prefixSum += nums[j]  # 略微改变求和的方式，减少计算
                if prefixSum == k:
                    res += 1
        return res

> Time Complexity O(N)
> Space Complexity O(N)
还记得two sum这道题么？其实我们大可以把preSum作为我们字典中的key，然后value设置成为preSum出现次数，
我们在迭代的时候，只需要查找preSum - target在不在字典里面，在的话，返回值增值即可，思路和two sum完全一样。
这里我们字典里之所以存储出现次数，是为了解决出现重复数字的问题，比如[0,0,0]这种case。
class Solution:
    def subarraySum(self, nums, target):
        dic = {0:1}
        res = pre_sum = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - target, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res



15. 3Sum
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l+=1
                    while l < r and nums[r] == nums[r+1]: r-=1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
