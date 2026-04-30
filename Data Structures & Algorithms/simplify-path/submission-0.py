class Solution:
    def simplifyPath(self, path: str) -> str:
        splitPath = path.split('/')
        stack = []
        for char in splitPath:
            if char == '.':
                continue
            elif char == '..' and len(stack) > 0:
                stack.pop()
            elif char != "" and char != '..':
                stack.append(char)
        print(stack)
        
        return '/' + '/'.join(stack)