
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
