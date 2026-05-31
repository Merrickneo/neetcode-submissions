class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # iterate through each row and do binary search if the target
        # is in the range
        # O(m) + O(logn)
        for row_index, row in enumerate(matrix):
            x, y = 0, len(row) -1
            if row[x] <= target <= row[y]:
                while x <= y:
                    middle = (x + y) // 2
                    if row[middle] == target:
                        return True
                    elif row[middle] < target:
                        x = middle + 1
                    else:
                        y = middle - 1
                return False
        return False
        