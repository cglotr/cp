class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        # base is the first number & left half of the palindrome. -1 math is needed
        # to handle odd & even lengths. for example, if intLength=2, then base=1.
        # if intLength=3, then base=10.
        base = 10 ** ((intLength - 1) // 2)
        
        res = []
        for query in queries:
            
            # to get the ith number we need to add (query - 1) to base. the -1 is because
            # base is the first number so we need to exclude it from query.
            number = base + (query - 1)
            
            # compute the upper bound. for example, base=10 (intLength=3) means the range of valid numbers
            # are between [10, 99].
            upper_bound = (base * 10) - 1
            
            # number goes beyond the bound which makes it invalid since the length
            # of the palindrome will no longer be of length intLength.
            if number > upper_bound:
                res.append(-1)
                continue
            
            s = str(number)
            
            # for even, the palindrome is s + s. for example, if s=12, then 12|21.
            # for odd, s + mid + s. for example, if s=123, then 12(3)|21.
            if intLength % 2 == 0:
                res.append(int(s + s[::-1]))
            else:
                res.append(int(s + s[:-1:][::-1]))
                
        return res
