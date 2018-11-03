class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            if mid*mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid*mid > x:
                r = mid
            else:
                l = mid + 1
                
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
