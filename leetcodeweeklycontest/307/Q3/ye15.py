# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = collections.defaultdict(list)
        stack = []
        stack.append((root, None))
        
        while stack:
            u, par = stack.pop()
            
            if par:
                graph[u.val].append(par.val)
                graph[par.val].append(u.val)
                
            if u.left:
                stack.append((u.left, u))
                
            if u.right:
                stack.append((u.right, u))
                
        queue = collections.deque()
        queue.append(start)
        
        seen = set()
        seen.add(start)
        
        ans = 0
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                u = queue.popleft()
                
                for v in graph[u]:
                    if v not in seen:
                        queue.append(v)
                        seen.add(v)
                        
            ans += 1
            
        return ans - 1
