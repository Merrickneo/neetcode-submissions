class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Monotonic stack is strictly increasing
        
        We need a way to track how many indexes ago was a smaller temperature was found
        + have to store the temperature and the index

        If we find a larger temperature as compared to the previously seen
        elements then we will record down the diff in the indexes

        monotonic stack: whereby the elements are strictly increasing temperatures. still in the stack means we have not matched with a future larger temperature

        '''
        n = len(temperatures)
        output = [0] * n
        stack = []
        for index, temperature in enumerate(temperatures):
            # check if we can pop and record down the diff
            while stack and stack[-1][0] < temperature:
                top, j = stack.pop()
                diff = index - j
                output[j] = diff
            stack.append((temperature, index))
        return output







        