class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # iterate through each row and do binary search if the target
        # is in the range
        # O(m) + O(logn)

        '''
        After we identify the particular row, perform binary search.
        Identify the specific row using binary search (low, high)
        '''
        low, high = 0, len(matrix) - 1
        while low <= high:
            middle = (low + high) // 2
            middle_row = matrix[middle]
            if middle_row[0] <= target <= middle_row[-1]:
                return self.binarySearch(middle_row, target)
            elif target < middle_row[0]:
                high = middle - 1
            else:
                low = middle + 1
        return False


    def binarySearch(self, row, target):
        x, y = 0, len(row) -1
        while x <= y:
            middle = (x + y) // 2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                x = middle + 1
            else:
                y = middle - 1
        return False

        