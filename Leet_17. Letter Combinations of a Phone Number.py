#  recursion 还是递归解法！！！

17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(dicts[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        last = dicts[digits[-1]]
        
        return [s+c for s in prev for c in last]
