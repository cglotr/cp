class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(target)
        i = 0
        j = 0
        
        while i < n:
            if target[i] == '_':
                i += 1
                continue
            
            while j < n and start[j] == '_':
                j += 1
                
            if j >= n:
                return False
            
            if start[j] != target[i]:
                return False
            
            if start[j] == 'L':
                if i > j:
                    return False
            else:
                if i < j:
                    return False
                
            i += 1
            j += 1
            
        while j < n:
            if start[j] != '_':
                return False
            j += 1
            
        return True
