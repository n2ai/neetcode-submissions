class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        ogColor = image[sr][sc]
        def dfs(r, c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != ogColor or
            image[r][c] == color):
                return 
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr,sc)

        return image