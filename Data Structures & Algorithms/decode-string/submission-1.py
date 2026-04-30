class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for char in s:
            if char == "]":
                temp = ''
                while stack[-1] != "[":
                    temp = (stack.pop()) + temp
                
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append (int(k) * temp)
            else:   
                stack.append(char)

        return (''.join(stack))
