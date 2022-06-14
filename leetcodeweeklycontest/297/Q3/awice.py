class Solution:
    def distributeCookies(self, A: List[int], k: int) -> int:        
        if k == len(A):
            return max(A)
        ans = math.inf
        for choice in itertools.product(range(k), repeat=len(A)):
            sums = [0 for _ in range(k)]
            for i, c in enumerate(choice):
                sums[c] += A[i]
            ans = min(ans, max(sums))
        return ans
