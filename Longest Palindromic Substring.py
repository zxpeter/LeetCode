class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        final_right = 0
        final_left = 0
        for i in range(len(s)):
            left = i-1 # odd
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_len = right - left
                if max_len < cur_len:
                    max_len = cur_len
                    final_left = left
                    final_right = right
                left -= 1
                right += 1

            left = i # even
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_len = right - left
                if max_len < cur_len:
                    max_len = cur_len
                    final_left = left
                    final_right = right
                left -= 1
                right += 1

        return s[final_left:final_right+1]

if __name__ == '__main__':
    sol = Solution()
    str = 'cbbd'
    str2 = 'babad'
    max_len= sol.longestPalindrome(str)

    print(max_len)



