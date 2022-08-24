class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = collections.defaultdict(int)
        
        for d in num:
            count[d] += 1
            
        odd = ''
        odd_v = -math.inf
        
        for d in count:
            if count[d] % 2 != 0 and int(d) > odd_v:
                odd = d
                odd_v = int(d)
                
        ans = odd
        
        for d in '0123456789':
            for _ in range(count[d] // 2):
                ans = d + ans + d
                
            count[d] -= 2 * (count[d] // 2)
                
        while len(ans) > 0 and ans[0] == '0' and ans[-1] == '0':
            ans = ans[1:-1]
            
        if len(ans) % 2 != 0:
            k = len(ans) // 2
            
            for d in '987654321':
                if count[d] > 0 and int(d) > int(ans[k]):
                    ans = ans[:k] + d + ans[k + 1:]
                
        if ans == '':
            for d in '9876543210':
                if count[d] > 0:
                    return d
                
            return '0'
                
        return ans
