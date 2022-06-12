class Solution:
    def minPathCost(self, A: List[List[int]], moveCost: List[List[int]]) -> int:
        R = len(A)
        C = len(A[0])
        
        @cache
        def dp(x, y):
            if x >= R - 1:
                return A[x][y]
            
            ans = math.inf
            v = A[x][y]
            
            for ny in range(C):
                ans = min(ans, v + moveCost[v][ny] + dp(x + 1, ny))
                
            return ans
        
        return min(dp(0, y) for y in range(C))
