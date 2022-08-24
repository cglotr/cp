class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = collections.defaultdict(int)
        
        for d in num:
            count[d] += 1
            
        left = ''
        
        for d in '9876543210':
            x = count[d] // 2
            left += d * x
            count[d] -= 2 * x
            
        left = left.lstrip('0')
        mid = ''
        
        for d in '9876543210':
            if count[d] > 0:
                mid = d
                break
                
        right = left[::-1]
        ans = left + mid + right
        
        return ans if ans else '0'
