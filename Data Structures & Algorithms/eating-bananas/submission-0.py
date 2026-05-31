from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        answer = -1
        i, j = 1, k
        while i <= j:
            middle = (i + j) // 2
            total_time = 0
            for pile in piles:
                total_time += ceil(pile / middle)
            if total_time <= h:
                answer = middle
                j = middle - 1
            else:
                i = middle + 1
        return answer