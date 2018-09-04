class Solution:
    def lengthOfLongestSubstring(self, s):
        # arr_all = []
        temp_arr = []
        res_len = 0
        for i in s:
            if i in temp_arr:
                index_dup = temp_arr.index(i)
                # arr_all.append(temp_arr)
                res_len = max(len(temp_arr), res_len)
                if index_dup < len(temp_arr):
                    temp_arr = temp_arr[index_dup+1:]
                    temp_arr.append(i)
            else:
                temp_arr.append(i)
        # arr_all.append(temp_arr)
        res_len = max(len(temp_arr), res_len)
        return res_len


if __name__ == '__main__':
    strexam = "aabaab!bb"
    res = Solution()
    res_len = res.lengthOfLongestSubstring(strexam)



