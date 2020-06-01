
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        x = len(board)
        if x == 0:
            return
        y = len(board[0])

        self.entry = []
        for i in range(x):
            if board[i][0] == 'O':
                self.entry.append((i, 0))
            if board[i][y - 1] == 'O':
                self.entry.append((i, y - 1))
        for i in range(y):
            if board[0][i] == 'O':
                self.entry.append((0, i))
            if board[x -1][i] == 'O':
                self.entry.append((x - 1, i))
        self.search(board, x, y)
        for i in board:
            print(i)

    def search(self, board, x, y):
        for entry in self.entry:
            self.dfs(board, entry, x, y)
        for i in range(x):
            for j in range(y):
                if board[i][j] != '-1':
                    board[i][j] = 'X'
        for i in range(x):
            for j in range(y):
                if board[i][j] == '-1':
                    board[i][j] = 'O'
        return board

    def dfs(self, board, entry, x, y):
        board[entry[0]][entry[1]] = '-1'
        es = []
        if entry[0] - 1 >= 0 and board[entry[0] - 1][entry[1]] == 'O':
            es.append((entry[0] - 1, entry[1]))
        if entry[0] + 1 < x and board[entry[0] + 1][entry[1]] == 'O':
            es.append((entry[0] + 1, entry[1]))
        if entry[1] - 1 >= 0 and board[entry[0]][entry[1] - 1] == 'O':
            es.append((entry[0], entry[1] - 1))
        if entry[1] + 1 < y and board[entry[0]][entry[1] + 1] == 'O':
            es.append((entry[0], entry[1] + 1))

        for i in es:
            self.dfs(board, i, x, y)



b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
b = []
s = Solution()
s.solve(b)