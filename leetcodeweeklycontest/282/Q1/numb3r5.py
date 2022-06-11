class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def f(x):
            a, b = map(int, x.split(':'))
            return a * 60 + b
        
        s = f(correct)-f(current)
        ans = 0
        
        for i in [60, 15, 5, 1]:
            x = s // i
            s %= i
            ans += x
        
        return ans
