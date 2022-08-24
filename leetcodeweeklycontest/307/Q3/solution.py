# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = collections.defaultdict(list)
        
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        q = collections.deque()
        q.append(start)
        
        seen = set()
        seen.add(start)
        
        level = 0
        
        while q:
            n = len(q)
            nq = collections.deque()
            
            for _ in range(n):
                u = q.popleft()
                
                for v in graph[u]:
                    if v not in seen:
                        nq.append(v)
                        seen.add(v)
                 
            if nq:
                level += 1
            q = nq
            
        return level
