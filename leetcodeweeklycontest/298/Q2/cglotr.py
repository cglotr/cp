class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        dp = [math.inf for _ in range(num+1)]
        dp[0] = 0
        for i in range(1, num+1):
            for j in range(1, i+1):
                d = j % 10
                if d == k:
                    cand = dp[i-j] + 1
                    if cand < dp[i]:
                        dp[i] = cand
        return dp[num] if dp[num] < math.inf else -1
