67. 机器人的运动轨迹
class Solution:
    def judge(self, threshold, i, j):
        if sum(map(int,str(i)+str(j))) <= threshold:
            return True
        else:
            return False

    def findgrid(self, threshold, rows, cols, matrix, i, j):
        count = 0
        if i<rows and j<cols and i>=0 and j>=0 and self.judge(threshold,i,j) and matrix[i][j]==0:
            matrix[i][j] = 1
            count = 1 + self.findgrid(threshold, rows, cols, matrix, i, j+1) \
            + self.findgrid(threshold, rows, cols, matrix, i, j-1) \
            + self.findgrid(threshold, rows, cols, matrix, i+1, j) \
            + self.findgrid(threshold, rows, cols, matrix, i-1, j)
        return count

    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        count = self.findgrid(threshold, rows, cols, matrix, 0, 0)
        print(matrix)
        return count

Word Search I

class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.DFS(board, i, j, word):
                    return True
        return False
    
    def DFS(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        res = self.DFS(board, i+1, j, word[1:]) or self.DFS(board, i-1, j, word[1:]) \
                or self.DFS(board, i, j+1, word[1:]) or self.DFS(board, i, j-1, word[1:])
        board[i][j] = temp
        return res
        

        
        
        
        
