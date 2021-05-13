class Node:

    def __init__(self, object):
        self.value = object
        self.next = None
        self.previous = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element, index):
        E = Node(element)
        if self.head is None:
            self.head = E
            self.tail = E
        elif index == 0:
            temp = self.head
            temp.previous = E
            E.next = temp
            self.head = E
        elif index >= self.size():
            temp = self.tail
            temp.next = E
            E.previous = temp
            self.tail = E
        elif index > self.size() / 2:
            temp = self.tail
            index = self.size() - index
            while index > 1:
                temp = temp.previous
                index -= 1
            E.previous = temp.previous
            E.next = temp
            temp.previous = E
            temp = E.previous
            temp.next = E
        elif index <= self.size() / 2:
            temp = self.head
            while index > 0:
                temp = temp.next
                index -= 1
            E.previous = temp.previous
            E.next = temp
            temp.previous = E
            temp = E.previous
            temp.next = E

    def remove(self, index):
        if self.size() > 0:
            if index == 0:
                self.head = self.head.next
            elif index == self.size():
                self.tail = self.tail.previous
                self.tail.next = None
            elif index <= self.size()/2:
                temp = self.head
                while index > 0:
                    temp = temp.next
                    index -= 1
                pre = temp.previous
                nex = temp.next
                nex.previous = pre
                pre.next = nex
            elif self.size() >= index >= self.size() / 2:
                temp = self.tail
                index = self.size() - index
                while index > 1:
                    temp = temp.previous
                    index -= 1
                nex = temp.next
                pre = temp.previous
                pre.next = nex
                nex.previous = pre
            else:
                print("Nie znaleziono elementu o takim indeksie.")
                print(f'Lista zawiera {self.size()} elementow.')

    def size(self):
        if self.head is not None:
            temp = self.head
            n = 1
            while temp.next:
                temp = temp.next
                n += 1
            return n
        else:
            return 0

    def getElement(self, index):
        if self.size() >= index >= self.size() / 2:
            temp = self.tail
            index = self.size() - index - 1
            while index > 0:
                temp = temp.previous
                index -= 1
        else:
            temp = self.head
            while index > 0:
                temp = temp.next
                index -= 1
        return temp

    def print(self):
        temp = self.head
        print(f'{temp.frequency}')
        while temp.next is not None:
            print(f'{temp.next.frequency}')
            temp = temp.next

    def indexOf(self, element, p, k):
        i = 0
        temp = self.head
        while i < p:
            temp = temp.next
            i += 1
        for i in range(p, k):
            if temp == element:
                print("sasa")
        return "Nie znaleziono elementu na liscie."


list = List()

list.add(4, 7)
list.add("X", 3)
list.add(3, 1)
list.add(5, 0)
list.add("L", 0)
list.add("V", 1)
list.add("O", 1)
list.add("E", 3)
list.add("&", 4)
list.remove(6)
print(list.indexOf(list.getElement(2), 0, list.size()))

for i in range(0, list.size()):
    print(list.getElement(i).frequency)
