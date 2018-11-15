Input: a = "11", b = "1"
Output: "100"
Input: a = "1010", b = "1011"
Output: "10101"

# life - time to learn recursion

class Solution:
    def addBinary(self, a, b):

        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'    
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        
        
        
