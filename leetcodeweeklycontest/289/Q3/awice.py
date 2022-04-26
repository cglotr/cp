class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=YczmyXzMWAM&t=1032s
        
        def log(*args):
            if 1:
                print(*args)
                
        R = len(grid)
        C = len(grid[0])
        
        def convert(x):
            two = five = 0
            
            # count twos
            while x % 2 == 0:
                two += 1
                x = x // 2
            
            # count fives
            while x % 5 == 0:
                five += 1
                x = x // 5
                
            return two + five * 1j
        
        A = [[convert(grid[r][c]) for c in range(C)] for r in range(R)]
        
        @cache
        def dp(r, c):
            if r < 0 or c < 0:
                return 0
            return A[r][c] + dp(r - 1, c) + dp(r, c - 1) - dp(r - 1, c - 1)
            
        res = 0
            
        for r in range(R):
            for c in range(C):
                up = dp(r, c) - dp(r, c - 1) - A[r][c]
                down = dp(R - 1, c) - dp(R - 1, c - 1) - dp(r - 1, c) + dp(r - 1, c - 1) - A[r][c]
                left = dp(r, c) - dp(r - 1, c) - A[r][c]
                right = dp(r, C - 1) - dp(r - 1, C - 1) - dp(r, c - 1) + dp(r - 1, c - 1) - A[r][c]
                
                for choice in combinations([up, down, left, right], 2):
                    cand = A[r][c] + sum(choice)
                    cand_zeros = int(min(cand.real, cand.imag))
                    res = max(res, cand_zeros)
                    
        return res
