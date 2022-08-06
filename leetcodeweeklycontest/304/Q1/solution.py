class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        
        while sum(nums) > 0:
            min_v = math.inf
            
            for x in nums:
                if x > 0:
                    min_v = min(min_v, x)
                    
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= min_v
                
            ans += 1
        
        return ans
