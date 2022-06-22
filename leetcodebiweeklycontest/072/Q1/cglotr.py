class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]
                if a == b and (i * j) % k == 0:
                    ans += 1
        return ans
