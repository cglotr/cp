class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        upper_sum = 0
        for upper, perc in brackets:
            upper -= upper_sum
            delta = min(income, upper)
            ans += delta * perc / 100
            income -= delta
            upper_sum += upper
        return ans
