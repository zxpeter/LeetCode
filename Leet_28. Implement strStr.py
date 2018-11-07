Input: haystack = "hello", needle = "ll"
Output: 2

class Solution(object):
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
    
    
    
class Solution: # 你看看你有多麻烦吧！！
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        i = j = 0
        while i < len(haystack):
            i = i - j
            j = 0
            while needle[j] == haystack[i]:
                if j == len(needle)-1:
                    return i-j
                if i == len(haystack)-1:
                    return -1
                j += 1
                i += 1
            i += 1
        if j != len(needle):
            return -1    
