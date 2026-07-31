class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        # dp[i+1] and dp[i+2]
        prev1 = 1  # dp[n]
        prev2 = 0  # placeholder for dp[n+1]

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = prev1  # Take one digit

                # Take two digits if valid
                if (
                    i + 1 < n
                    and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'))
                ):
                    curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1