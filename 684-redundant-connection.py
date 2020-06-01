#*.*coding:utf-8

# union find
# 继续并查集, 有向图，按序合并集合，当当前边的两个定点属于同一集合时则该边为冗余边
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = 0
        for i in edges:
            if N < max(i):
                N = max(i)
        self.data = range(N + 1)

        redundant = []
        for ed in edges:
            rded = self.union(ed[0], ed[1])
            if rded is not None:
                redundant.append(rded)

        return redundant[0]

    def union(self, x, y):
        if x != y:
            tpe = self.find(x)
            if tpe != self.find(y):
                self.data[tpe] = self.data[y]
                return None
            else:
                return [x, y]

    def find(self, i):
        if self.data[i] != i:
            self.data[i] = self.find(self.data[i])
        return self.data[i]


if __name__ == '__main__':
    solution = Solution()
    data = [
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
        [[1, 2], [1, 3], [2, 3]]
    ]
    # [1,4]
    # [2,3]

    for i in data:
        print(solution.findRedundantConnection(i))
