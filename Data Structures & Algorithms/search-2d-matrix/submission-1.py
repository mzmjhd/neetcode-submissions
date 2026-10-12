class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        #find rows
        top = 0
        bot = ROWS - 1
        while (top <= bot):
            row = top + ((bot - top)//2)
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                #binary search inside row
                l,r = 0, COLS-1
                while (l<=r):
                    m = l + ((r-l)//2)
                    print(row,l,m,r)
                    if matrix[row][m] > target:
                        r = m-1
                    elif matrix[row][m] < target:
                        l = m+1
                    else:
                        return True
                return False
        return False