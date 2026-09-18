class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute force solution: For each start num, we see if we can 
        get the num + x chain whereby x is the number of elements
        to the right. Ans is x + 1

        hashMap will store the possible start points
        - Start point is that num - 1 is not seen so far
        - Accumulate all these and then for each key, we see for key + i 
        and see what's the largest consecutive sequence length
        Eg [3,1,2]
        key[3] = 1, found:
        key[1] = 1, found: 2, 3 -> 3
        key[2] = 1, found: 3 -> 2


        This solution does not pass as in the worst case its O(n^2)
        - [10, 9, 8..., 1]
        - 10 possible start points based on this

        then we iterate for potentially n - 1 elements up
        '''
        # Initialise a set for easy look up
        num_set = set(nums)
        potential_start_points = []
        for num in nums:
            if num - 1 not in num_set:
                potential_start_points.append(num)
        output = 0
        for start in potential_start_points:
            i = 0
            while start + i in num_set:
                i += 1
            output = max(output, i)
        return output

        