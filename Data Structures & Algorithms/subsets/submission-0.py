class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(start_index, current):
            output.append(list(current))
            for i in range(start_index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return output
        