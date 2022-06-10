class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def time(s):
            h, m = s.split(':')
            return int(h) * 60 + int(m)
        
        s = time(current)
        e = time(correct)
        
        def calc(mins):
            ans = 0
            
            for div in [60, 15, 5, 1]:
                ans += mins // div
                mins = mins % div
            
            return ans
        
        return calc(e - s)
