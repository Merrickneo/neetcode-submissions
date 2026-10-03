import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We can store the euclidean distance as the key which will be used to sort
        # After populating into the minHeap we can return the k points
        closest_points = []
        for point in points:
            euclidean_distance = sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(closest_points, (-euclidean_distance, point))
            # We can just store k values inside the minHeap
            if len(closest_points) > k:
                heapq.heappop(closest_points)
        output = []
        for i in range(k):
            point = closest_points[i]
            output.append(point[1])
        return output
            
            

        