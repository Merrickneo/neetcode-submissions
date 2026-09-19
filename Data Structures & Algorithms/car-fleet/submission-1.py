class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_car_list = list(zip(position, speed))
        position_car_list.sort(key = lambda x: x[0], reverse=True)
        stack = []
        for p, s in position_car_list:
            time_taken = (target - p) / s
            if stack:
                if time_taken <= stack[-1]:
                    continue
            stack.append(time_taken)
        return len(stack)
        