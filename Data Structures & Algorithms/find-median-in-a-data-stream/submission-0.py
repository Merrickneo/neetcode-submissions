import heapq
class MedianFinder:
    '''
    If the list is even, the answer is the average of the middle two elements.
    I think we could make use of two heaps
    - Max Heap for the smaller half
    - Min Heap for the larger half

    - We have to make the two balanced
    - We add into the smaller half first, then we pop the largest and add it into the larger heap
    if they differ more than size =1
    '''
    def __init__(self):
        self.heap_small, self.heap_large = [], []
        heapq.heapify(self.heap_small)
        heapq.heapify(self.heap_large)

    def addNum(self, num: int) -> None:
        # have to check which heap to add to
        if not self.heap_small:
            heapq.heappush(self.heap_small, -num)
            return
        largest_small = -self.heap_small[0]
        if largest_small <= num:
            heapq.heappush(self.heap_large, num)
            if len(self.heap_large) > len(self.heap_small) :
                elem = heapq.heappop(self.heap_large)
                heapq.heappush(self.heap_small, -elem)
        else:
            heapq.heappush(self.heap_small, -num)
            if len(self.heap_small) - len(self.heap_large) > 1:
                elem = -heapq.heappop(self.heap_small)
                heapq.heappush(self.heap_large, elem)
    
        

    def findMedian(self) -> float:
        if len(self.heap_small) - len(self.heap_large) > 0:
            return -self.heap_small[0]
        return (-self.heap_small[0] + self.heap_large[0]) / 2
        
        