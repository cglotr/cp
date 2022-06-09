class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        cur_min = nums[0]
        for x in nums[1:]:
            diff = x - cur_min
            if diff <= k:
                continue
            ans += 1
            cur_min = x
        return ans + 1
