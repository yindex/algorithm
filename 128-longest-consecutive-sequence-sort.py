class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return  0
        nums = sorted(nums)
        self.data = range(len(nums))
        self.st = set()
        for i in range(0, len(nums) - 1, 1):
            if nums[i] - nums[i+1] == -1:
                self.data[i+1] = self.data[i]
            if nums[i] == nums[i+1]:
                self.data[i+1] = self.data[i]
                self.st.add(i+1)

        s = [0] * len(nums)
        for i in range(len(self.data)):
            if i not in self.st:
                s[self.data[i]] += 1
        return max(s)

s = Solution()
print(s.longestConsecutive([0,0,-1, 0]))
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([1,2,0,1]))
# 0 1 1 2
#100,4,200,1,3,2
# 0 1 2 3 4 5
# 0 1 2 3 1 2
# 0 1 2 3 1 3
# 0 1 2 3 1