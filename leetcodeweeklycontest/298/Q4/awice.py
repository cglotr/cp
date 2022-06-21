class Solution:
    def sellingWood(self, H, W, prices) -> int:
        dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
        for h, w, v in prices:
            dp[h][w] = v
        for h in range(1, H+1):
            for w in range(1, W+1):
                for i in range(1, h):
                    cand = dp[h-i][w] + dp[i][w]
                    if cand > dp[h][w]:
                        dp[h][w] = cand
                for i in range(1, w):
                    cand = dp[h][w-i] + dp[h][i]
                    if cand > dp[h][w]:
                        dp[h][w] = cand
        return dp[H][W]
