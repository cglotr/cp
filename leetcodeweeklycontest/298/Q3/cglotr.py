class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        while int(s, 2) > k:
            i = s.index('1')
            s = s[:i] + s[i+1:]
        return len(s)
