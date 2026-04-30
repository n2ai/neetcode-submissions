class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s:
            if i in parenMap:
                if stack and stack[-1] == parenMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False