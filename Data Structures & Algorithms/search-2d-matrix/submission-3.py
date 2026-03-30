class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bigm = len(matrix)//2
        rows, cols = len(matrix), len(matrix[0])
        start = 0
        end = rows - 1 #put cols instead of rows here
        while start <= end:
            bigm = (start + end)//2
            print(bigm)
            if matrix[bigm][0] > target:
                end = bigm - 1
            elif matrix[bigm][-1] < target: 
                start = bigm + 1
            else:
                break

        if start > end: #didn't have this conditional so it wasn't running right
            return False

        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r)//2
            if matrix[bigm][m] < target:
                l = m + 1
            elif matrix[bigm][m] > target: 
                r = m - 1
            elif matrix[bigm][m] == target:
                return True
        return False



