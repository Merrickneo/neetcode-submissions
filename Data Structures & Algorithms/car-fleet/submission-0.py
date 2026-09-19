class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        n cars start at different positions and speeds
        - For each of the cars we check if we reach the same position as any of the cars before it.
        - If same position then we adjust that car's speed to the fleet before

        We could make use of a stack to keep track the position and speed of the a car
        that reached that particular position
        + If the next car reaches that same position then we we merge them together

        + We will iterate through the elements in the stack
        + Monotonically decreasing
        '''
        position_speed_array = list(zip(position, speed))
        position_speed_array.sort(key=lambda x: x[0], reverse = True)
        stack = []
        for position, speed in position_speed_array:
            dist_left = target - position
            # if need exact time then do math.ceil (import math)
            time_taken = dist_left / speed
            if stack:
                prev_fleet = stack[-1]
                if time_taken <= prev_fleet:
                    continue
            stack.append(time_taken)
        return len(stack)
            
        


        