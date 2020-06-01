class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        L, R, U, D = 0, 0, 0, 0
        for action in moves:
            if action == "L":
                L +=1
            if action == "R":
                R +=1
            if action == "U":
                U += 1
            if action == "D":
                D += 1
        return (abs(L-R) + abs(U-D)) == 0

s = Solution
print(s.judgeCircle())
print(s.judgeCircle("RR"))
print(s.judgeCircle("UD"))
print(s.judgeCircle("RL"))
print(s.judgeCircle("RL"))