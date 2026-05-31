class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        sorted_dict = sorted(counter.items(), key = lambda counter: counter[1], reverse=True)
        count = 0
        output = []
        for key, value in sorted_dict:
            if count < k:
                output.append(key)
            count += 1
        return output
