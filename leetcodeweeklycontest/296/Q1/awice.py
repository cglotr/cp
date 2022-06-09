class Solution:
    def minMaxGame(self, A: List[int]) -> int:
        if len(A) < 1:
            return 0
        if len(A) == 1:
            return A[0]
        B = []
        for i in range(0, len(A), 2):
            # (i/2)%2 = i%4
            if i % 4 == 0:
                B.append(min(A[i], A[i + 1]))
            else:
                B.append(max(A[i], A[i + 1]))
        return self.minMaxGame(B)
