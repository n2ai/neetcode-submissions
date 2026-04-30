class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                val1 = stack.pop()
                val2 = stack.pop()

                newVal = val2 + val1
                stack.append(newVal)
            elif char == "-":
                val1 = stack.pop()
                val2 = stack.pop()

                newVal = val2 - val1
                stack.append(newVal)
            elif char == "*":
                val1 = stack.pop()
                val2 = stack.pop()

                newVal = val2 * val1
                stack.append(newVal)
            elif char == "/":
                val1 = stack.pop()
                val2 = stack.pop()

                newVal = int(val2 / val1)
                stack.append(newVal)
            else:
                stack.append(int(char))
        
        return stack[0]