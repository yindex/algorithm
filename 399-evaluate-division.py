class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.tab = dict()
        cursor = 0
        for pos in equations:
            if pos[0] not in self.tab:
                self.tab[pos[0]] = cursor
                cursor += 1
            if pos[1] not in self.tab:
                self.tab[pos[1]] = cursor
                cursor += 1

        self.data = [['?' for i in range(len(self.tab))] for i in range(len(self.tab))]
        self.visit = [[0 for i in range(len(self.tab))] for i in range(len(self.tab))]

        for i in range(len(equations)):
            x = self.tab[equations[i][0]]
            y = self.tab[equations[i][1]]
            self.data[x][y] = values[i]
            self.data[y][x] = 1.0 / values[i]
        for ps in equations:
            self.search(self.tab[ps[0]], self.tab[ps[1]])
            self.search(self.tab[ps[1]], self.tab[ps[0]])

        s = []
        for param in queries:
            if param[0] not in self.tab or param[1] not in self.tab:
                s.append(-1.0)
            else:
                if self.data[self.tab[param[0]]][self.tab[param[1]]] != '?':
                    s.append(self.data[self.tab[param[0]]][self.tab[param[1]]])
                else:
                    s.append(-1.0)
        return s

    def search(self, x, y):
        if self.visit[x][y] == 1:
            return
        else:
            self.visit[x][y] = 1

        for i in range(len(self.data[y])):
            if self.data[y][i] != '?':
                self.data[x][i] = self.data[y][i] * self.data[x][y]
                self.search(x, i)




# [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
# [3.0,0.5,3.4,5.6]
# [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
# [1.13333,16.8,1.5,1.0,0.05952,2.26667,0.44118,-1.0,-1.0]
s = Solution()
p = s.calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]], [3.0,0.5,3.4,5.6],
               [["x2", "x4"], ["x1", "x5"], ["x1", "x3"], ["x5", "x5"], ["x5", "x1"], ["x3", "x4"], ["x4", "x3"],
                ["x6", "x6"], ["x0", "x0"]])

print(p)