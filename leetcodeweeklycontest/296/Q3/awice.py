class Solution:
    def arrayChange(self, A: List[int], operations: List[List[int]]) -> List[int]:
        loc = {v: i for i, v in enumerate(A)}
        
        for u, v in operations:
            i = loc[u]
            A[i] = v
            loc[v] = i
            
        return A
