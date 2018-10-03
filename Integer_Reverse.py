class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            res = int(str(x)[::-1])
            if res <= 0x7FFFFFFF:
                return res
            else:
                return 0
        else:
            res = -int(str(x)[:0:-1])
            if res >= -0x7FFFFFFF:
                return res
            else:
                return 0

    def reverse2(self, x):
        if x < 0:
            return -self.reverse2(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.
    
if __name__ == '__main__':
    sol = Solution()
    num = -2147483648
    res = sol.reverse(num)
    print(res)

