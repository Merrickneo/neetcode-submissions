class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(open, close, output):
            if open == 0 and close == 0:
                combinations.append(output)
                return
            if open != 0:
                output1 = output + "("
                helper(open - 1, close, output1)
            if (open < close):
                output2 = output + ")"
                helper(open, close - 1, output2)
        
        combinations = []
        helper(n, n, "")
        return combinations
            

        