class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsDict = defaultdict(set)
        rowsDict = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in colsDict[c] or 
                    board[r][c] in rowsDict[r] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                colsDict[c].add(board[r][c])
                rowsDict[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
            
        return True
                    