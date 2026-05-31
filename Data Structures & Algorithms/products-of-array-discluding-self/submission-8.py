from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize prefix and postfix arrays
        prefix = [1] * n
        postfix = [1] * n
        
        # Fill the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Fill the postfix array
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        # Construct the output array
        output = [1] * n
        for i in range(n):
            output[i] = prefix[i] * postfix[i]
        
        return output




        