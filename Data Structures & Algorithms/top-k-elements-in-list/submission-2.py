import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        heapq.heapify(min_heap)
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        for key, freq in num_dict.items():
            heapq.heappush(min_heap, (freq, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [key for freq, key in min_heap]
        
        