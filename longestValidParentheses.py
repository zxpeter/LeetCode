class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        res = 0
        max_m = 0
        new_list = []
        for i in range(len(s)):
            if s[i] == '(':
                new_list.append(i)
            elif s[i] == ')':
                if not new_list:
                    start = i + 1
                    continue
                else:
                    new_list.pop()
                    if new_list:
                        res = max(res, i - new_list[-1])
                    else:
                        res = max(res, i - start + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    str = "()(()"
    print(sol.longestValidParentheses(str))






