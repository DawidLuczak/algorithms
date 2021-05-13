class Stack:

    top = 0

    def __init__(self, n):
        self.stack = []
        if n > 0:
            self.size = n
        else:
            self.size = float('inf')

    def isEmpty(self):
        if not self.stack:
            print("Stos jest pusty.")
            return True
        else:
            return False

    def isFull(self):
        if self.top < self.size:
            return False
        else:
            print("Stos jest pelny.")
            return True

    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
            self.top += 1
            print(f'Pushed: {item}')

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if not self.isEmpty():
            self.stack.reverse()
            x = self.stack[0]
            self.stack.remove(x)
            self.top -= 1
            self.stack.reverse()
            print(f'Poped: {x}')
            return x
