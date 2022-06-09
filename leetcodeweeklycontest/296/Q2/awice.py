class Solution:
    def partitionArray(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 0
        i = 0
        
        while i < len(A):
            ans += 1
            j = i
            
            while j < len(A) and A[j] <= A[i] + k:
                j += 1
                
            i = j
            
        return ans
