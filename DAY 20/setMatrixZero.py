class Solution:
    def setMatrixZero(self,matrix):
        rows=set()
        col=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    if i in rows or j in col:
                        matrix[i][j]=0
        return matrix
    
sol =Solution()
print(sol.setMatrixZero([[1,2,3],
                        [1,0,5],
                        [1,0,0]]))
                    