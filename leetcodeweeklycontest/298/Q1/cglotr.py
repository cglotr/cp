class Solution:
    def greatestLetter(self, s: str) -> str:
        cands = set()
        for c in s:
            if c.isupper():
                cands.add(c)
        ans = []
        A = set(s)
        for cand in cands:
            if cand.lower() in A:
                ans.append(cand)
        ans.sort()
        if len(ans) <= 0:
            return ''
        return ans[-1]
