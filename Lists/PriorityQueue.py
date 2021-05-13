class PriorityQueue:

    head: int
    tail: int
    queue: []

    def __init__(self, n):
        self.queue = [0 for i in range(0, n + 1)]
        self.size = n
        self.head = 0
        self.tail = 0

    def isFull(self):
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size):
            print("Kolejka jest pelna.")
            return True
        else:
            return False

    def isEmpty(self):
        if self.head == self.tail:
            print("Kolejka jest pusta.")
            return True
        else:
            return False

    def enqueue(self, node):
        if not self.isFull():
            self.queue[self.tail] = node
            if self.tail < self.size:
                self.tail += 1
            else:
                self.tail = 0
            print(f'Enqueue: {node}')

    def dequeue(self):
        if not self.isEmpty():
            x = self.queue[self.head]
            for i in range(self.head, self.size + 1):
                if self.queue[i] > x:
                    x = self.queue[i]
                    n = i
                    self.queue[n], self.queue[self.head] = self.queue[self.head], self.queue[n]

            if self.head < self.size:
                self.head += 1
            else:
                self.head = 0
            print(f'Dequeue: {x}')
            return x

