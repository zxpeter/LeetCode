9. Palindrome Number
class Solution:
    def isPalindrome(self, x):  # 数值解法
        if x < 0:
            return False
        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) / 10
            ranger /= 100
        return True
        
        
class Solution(object):   # 牛逼解法
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])
        
        
class Solution:  # 自己的傻乎乎常规操作
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        len_x = len(x)
        mid = len_x // 2
        if len_x == 1:
            return True
        elif len_x == 2:
            if x[mid-1] == x[mid]:
                return True
            else:
                return False
        
        if len_x % 2 == 0:  # even
            i, j = mid-1, mid
            while i >= 0 and j < len_x:
                print(x[i],x[j])
                print(i,j)
                if x[i] == x[j]:
                    i -= 1
                    j += 1
                else:
                    return False
                
        else:  # odd
            i, j = mid-1, mid+1
            while i >= 0 and j < len_x:
                if x[i] == x[j]:
                    i -= 1
                    j += 1
                else:
                    return False
        return True
