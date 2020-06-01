# *.* coding:utf-8
# 前缀数组
# 字符串x0 x1 x2 x3 ... xn
# 当字符串 xi-xj 包含xj+1时， 那么xi - xj 一定不重复。
#


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        self.last = {}
        self.data = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] in self.last:
                if self.last[s[i]] + 1 > self.data[i - 1]:
                    self.data[i] = self.last[s[i]] + 1
                else:
                    self.data[i] = self.data[i - 1]
            else:
                if i == 0:
                    self.data[i] = 0
                else:
                    self.data[i] = self.data[i - 1]
            self.last[s[i]] = i
        for i in range(len(self.data)):
            self.data[i] = i - self.data[i] + 1
        return max(self.data)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("abba"))












