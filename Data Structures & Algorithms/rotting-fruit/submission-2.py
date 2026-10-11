class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        DIRS = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        levels = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])

        #BFS
        while q:
            qLen = len(q)
            rotted = False
            for i in range(qLen):
                r,c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    rotted = True
            if rotted:
                levels += 1
        
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == 1:
                    return -1
        
        return levels