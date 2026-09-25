class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1  # s[0] is already known to be non-zero

        for i in range(2, n + 1):
            one_digit = s[i-1]
            two_digit = s[i-2:i]

            if one_digit != '0':
                dp[i] += dp[i-1]

            if '10' <= two_digit <= '26':
                dp[i] += dp[i-2]

        return dp[n]