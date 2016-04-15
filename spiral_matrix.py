"""
spiral matrix就是回型矩阵，例如输入n=3时，矩阵为：
1 2 3
8 9 4
7 6 5
"""
"""
具体的思路就是按照上下左右依次画出外围，画完一圈后，上下左右的指标都靠内增加/减少，再画一圈
那么一个周期就是4，direct来代表方向，0，1，2，3分别代表上方，右方，下方，左方
"""
class Solution:
    def generateMatrix(self, n):
        if n == 0: return []
        matrix = [[0 for i in range(n)] for j in range(n)]# 画0矩阵的好方法
        up = 0; down = len(matrix)-1# 上方的index是0，下方的index是矩阵列数-1，因为python中矩阵指标从(0,0)开始
        left = 0; right = len(matrix[0])-1# 左方的index是（0，列指标），右方是（行数-1，列指标）
        direct = 0; count = 0 #count作为计数器，从1开始到n**2结束
        while True:
            if direct == 0:#在上方从左往右画
                for i in range(left, right+1):
                    count += 1; matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    count += 1; matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    count += 1; matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    count += 1; matrix[i][left] = count
                left += 1
            if count == n*n: return matrix
            direct = (direct+1) % 4

ans = Solution()
ans.generateMatrix(int(raw_input('please input a number:')))
