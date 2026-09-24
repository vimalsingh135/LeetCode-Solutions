class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        rows,cols=set(),set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
           for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j]=0
        
