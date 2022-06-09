class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = dict()
        for i, x in enumerate(nums):
            index_map[x] = i
        for old, new in operations:
            i = index_map[old]
            nums[i] = new
            del index_map[old]
            index_map[new] = i
        return nums
