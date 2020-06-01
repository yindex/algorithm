class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        self.lands = []
        self.height = len(grid)
        if self.height == 0:
            return 0
        else:
            self.width = len(grid[0])

        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == "1":
                    self.lands.append((i, j))

        self.search(grid)
        s = set()
        for i in grid:
            for j in i:
                if j != '0' and j != '1':
                    s.add(j)

        return len(s)


    def search(self, grid):
        count = 0
        for i in self.lands:
            if grid[i[0]][i[1]] == '1':
                grid[i[0]][i[1]] = count
                count += 1
                self.dfs(i, grid)

    def dfs(self, entry, grid):
        # if grid[entry[0]][entry[1]] != '0' and grid[entry[0]][entry[1]] != '1':
        #     return

        es = []
        if entry[0] - 1 >= 0 and grid[entry[0] - 1][entry[1]] == '1':
            es.append((entry[0] - 1, entry[1]))
            grid[entry[0] - 1][entry[1]] = grid[entry[0]][entry[1]]

        if entry[0] + 1 < self.height and grid[entry[0] + 1][entry[1]] == '1':
            es.append((entry[0] + 1, entry[1]))
            grid[entry[0] + 1][entry[1]] = grid[entry[0]][entry[1]]
        if entry[1] - 1 >= 0 and grid[entry[0]][entry[1] - 1] == '1':
            es.append((entry[0], entry[1] - 1))
            grid[entry[0]][entry[1] - 1] = grid[entry[0]][entry[1]]
        if entry[1] + 1 < self.width and grid[entry[0]][entry[1] + 1] == '1':
            es.append((entry[0], entry[1] + 1))
            grid[entry[0]][entry[1] + 1] = grid[entry[0]][entry[1]]

        for i in es:
            self.dfs(i, grid)


d = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(d))