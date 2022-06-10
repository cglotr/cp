class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        INF = 10 ** 12
        
        lo = 1
        hi = INF
        
        def possible(x):
            ans = 0
            for p in candies:
                ans += p // x
            return ans >= k
        
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if possible(mid):
                lo = mid + 1
            else:
                hi = mid
                
        return lo - 1
