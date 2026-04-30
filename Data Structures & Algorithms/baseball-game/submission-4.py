class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            elif char == "D":
                val = stack[-1] * 2
                stack.append(val)
            elif char == "C":
                stack.pop()
            else:
                stack.append(int(char))
        return sum(stack)