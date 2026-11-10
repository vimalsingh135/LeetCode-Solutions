class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])
        low=0
        high=n*m-1
        while low<=high:
            guess=(low+high)//2
            row=guess//m
            cols=guess%m
            if matrix[row][cols]==target:
                return True
            if matrix[row][cols]<target:
                low=guess+1
            else:
                high=guess-1
        return False
        