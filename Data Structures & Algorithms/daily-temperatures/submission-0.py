class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [ 0 for _ in range(len(temperatures))]
        stack = []
        for index, val in enumerate(temperatures):
            if len(stack) > 0:
                
                while len(stack) > 0 and stack[-1][0] < val:
                    lastIndex = stack[-1][1]
                    
                    res[lastIndex] = index - lastIndex
                    stack.pop()
                
                stack.append([val,index])
            else:
                stack.append([val, index])

        return res