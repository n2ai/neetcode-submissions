class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            row = (top + bot)//2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) //2
        left = 0
        right = COLS - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False


            
        