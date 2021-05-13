class Queue:

    head = 0
    tail = 0
    queue: []

    def __init__(self, n):
        self.queue = [0 for i in range(0, n + 1)]
        self.size = n

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

    def enqueue(self, item):
        if not self.isFull():
            self.queue[self.tail] = item
            if self.tail < self.size:
                self.tail += 1
            else:
                self.tail = 0
            print(f'Enqueue: {item}')

    def dequeue(self):
        if not self.isEmpty():
            x = self.head
            if self.head < self.size:
                self.head += 1
            else:
                self.head = 0
            print(f'Dequeue: {self.queue[x]}')
            return self.queue[x]



