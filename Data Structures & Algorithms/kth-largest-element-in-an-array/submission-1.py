import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Trivial:
        Iterate through all the nums then return the kth element

        Make use of a minHeap and store only k elements
        '''
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

        