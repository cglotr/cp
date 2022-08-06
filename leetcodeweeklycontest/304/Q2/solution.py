class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)
        
        prev = 1
        prev_sum = grades.pop()
        ans = 1
        
        while grades:
            cur = 0
            cur_sum = 0
            
            while grades and (cur <= prev or cur_sum <= prev_sum):
                cur += 1
                cur_sum += grades.pop()
                
            if cur <= prev or cur_sum <= prev_sum:
                return ans
            
            prev = cur
            prev_sum = cur_sum
            
            ans += 1
            
        return ans
