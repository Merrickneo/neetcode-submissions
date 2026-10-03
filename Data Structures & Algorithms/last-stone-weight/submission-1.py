import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Make use of a maxHeap so that we can get the largest 2 elements at each time

        Initialisation + Operations will be O(nlogn)
        
        Return when there is 1 element or 0 elements in the maxHeap
        '''
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            # 2 stones
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            new_weight = 0
            if x == y:
                continue
            elif x < y:
                new_weight = y - x
            else:
                new_weight = x - y
            heapq.heappush(stones, -new_weight)
        if stones:
            return -stones[0]
        return 0

        