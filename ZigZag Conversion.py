
# 自顶向下的增加遍历，注意第20行 虽然越界，但是不保证下面的也越界
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        index = numRows - 1
        first = []
        second = []
        m = 0
        while m < len(s):
            first.append(m)
            second.append(m)
            m += index * 2
        first.append(m)
        n = 1
        for j in range(index):
            for i in first:
                if i - n > 0 and i - n < len(s):
                    if i-n != second[-1]:
                        second.append(i-n)
                if i + n < len(s):
                        second.append(i+n)

            n+=1
        res = []
        for i in second:
            res.append(s[i])
        res_str = ''.join(res)
        return res_str



if __name__ == '__main__':
    sol = Solution()
    s = 'PAYPALISHIRING'
    num = 3
    res = sol.convert(s, num)
    print(res)

