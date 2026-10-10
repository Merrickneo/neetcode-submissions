class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(i, current):
            if i == len(nums):
                output.append(list(current))
                return
            # Choice 1: Exclude current num
            helper(i + 1, current)

            # Choice 2: Include current num
            current.append(nums[i])
            helper(i + 1, current)
            current.pop()
        helper(0, [])
        return output