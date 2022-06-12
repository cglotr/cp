class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0.0
        prev_upper = 0
        for upper, percent in brackets:
            if income >= prev_upper:
                tax = (min(upper, income) - prev_upper) * (percent / 100)
                ans += tax
            prev_upper = upper
        return ans
