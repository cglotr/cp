class Solution:
    def maximumEvenSplit(self, final_sum: int) -> List[int]:
        if final_sum % 2 != 0:
            return []
        want = final_sum // 2
        ans = []
        x = 1
        cur_sum = 0
        while cur_sum + x <= want:
            ans.append(x)
            cur_sum += x
            x += 1
        ans[-1] += want - cur_sum
        return [i * 2 for i in ans]
