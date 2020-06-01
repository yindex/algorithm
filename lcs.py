class LCS:
	    def lcs(self, source, pattern):
        if len(source) == 0 or len(pattern) == 0:
            return ""
        max_length = 0
        pos = 0
        bit = [[0 for i in range(len(pattern))] for j in range(len(source))]
        for i in range(len(source)):
            for j in range(len(pattern)):
                if (i == 0 or j == 0) and source[i] == pattern[j]:
                    bit[i][j] = 1
                elif source[i] == pattern[j]:
                    bit[i][j] = bit[i - 1][j - 1] + 1
                else:
                    bit[i][j] = 0

                if bit[i][j] >= max_length:
                    max_length = bit[i][j]
                    pos = i
        print(max_length, pos)
        return source[pos + 1 - max_length: pos + 1]
