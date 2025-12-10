class MinStack:

    def __init__(self):
        self.main = []
        self.min = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.min or self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.main[-1]:
            self.min.pop()
        self.main.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())