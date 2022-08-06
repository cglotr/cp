class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        seen = {-1}
        n = len(edges)
        ans = -1
        
        for u in range(n):
            if u in seen:
                continue
                
            path = [u]
            seen.add(u)
            
            while edges[path[-1]] not in seen:
                path.append(edges[path[-1]])
                seen.add(path[-1])
                
            if edges[path[-1]] != -1:
                for i, node in enumerate(path):
                    if node == edges[path[-1]]:
                        sz = len(path) - i
                        ans = max(ans, sz)
                        
        return ans
