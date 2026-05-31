class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        # return the indices
        index = 0
        while index < len(numbers):
            if numbers[index] not in num_dict:
                num_dict[target - numbers[index]] = index + 1
            else:
                return [num_dict.get(numbers[index]), index + 1]
            index += 1
        return None

        