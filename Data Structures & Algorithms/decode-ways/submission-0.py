class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]== "0":
            return 0
        i = len(s) - 1
        dp = {len(s): 1}

        while i >= 0:
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
            i -= 1

        return dp[0]    