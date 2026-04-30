class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            flagBr = 0
            while (len(stack) > 0) and (stack[-1] > 0 and ast < 0):
                if abs(stack[-1]) > abs(ast):
                    flagBr = 1
                    break
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                else:
                    flagBr = 1
                    stack.pop()
                    break
            
            if flagBr == 0:
                stack.append(ast)
        return stack


