class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting empty string to/from a string of length k takes k inserts/deletes
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # chars match, no op needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete from word1
                        dp[i][j - 1],      # insert into word1
                        dp[i - 1][j - 1]   # replace
                    )
        
        return dp[m][n]