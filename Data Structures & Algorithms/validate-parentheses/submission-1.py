class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reverseSet = set(["}", "]", ")"])
        charMap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for char in s:
            if char in reverseSet:
                if len(stack) > 0 and charMap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False