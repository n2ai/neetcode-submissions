class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = list(zip(position, speed))
        arr.sort(key=lambda tup: tup[0], reverse=True)
        stack = []
        for val in arr:
            time = (target - val[0])/val[1]
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        
        return len(stack)