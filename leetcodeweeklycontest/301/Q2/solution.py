class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.added = set()

    def popSmallest(self) -> int:
        if len(self.added):
            x = min(self.added)
            self.added.remove(x)
            return x
        
        x = self.current
        self.current += 1
        
        return x

    def addBack(self, num: int) -> None:
        if num < self.current:
            self.added.add(num)
