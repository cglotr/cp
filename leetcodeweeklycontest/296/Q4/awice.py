class TextEditor:

    def __init__(self):
        self.s = ''
        self.i = 0

    def addText(self, text: str) -> None:
        i = self.i
        self.s = self.s[:i] + text + self.s[i:]
        self.i += len(text)

    def deleteText(self, k: int) -> int:
        i = self.i
        h = max(i - k, 0)
        self.s = self.s[:h] + self.s[i:]
        self.i = h
        return (i - h)

    def cursorLeft(self, k: int) -> str:
        self.i = max(self.i - k, 0)
        i = self.i
        h = max(0, i - 10)
        return self.s[h:i]

    def cursorRight(self, k: int) -> str:
        self.i = min(self.i + k, len(self.s))
        i = self.i
        h = max(0, i - 10)
        return self.s[h:i]
