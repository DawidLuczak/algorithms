class Node:

    def __init__(self, object):
        self.value = object
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, element, index):
        E = Node(element)
        if self.head is None:
            self.head = E
        elif index == 0:
            E.next = self.head
            self.head = E
        else:
            temp = self.head
            while temp.next is not None and index > 1:
                temp = temp.next
                index -= 1
            if temp.next is not None:
                E.next = temp.next
            temp.next = E

    def remove(self, index):
        if self.size() > 0:
            if index == 0:
                self.head = self.head.next
            elif index < self.size():
                i = 0
                temp = self.head
                while i < index:
                    temp = temp.next
                    i += 1
                if index < self.size():
                    nx = temp.next
                    i = 0
                    temp = self.head
                    while i < index - 1:
                        temp = temp.next
                        i += 1
                    temp.next = nx
                else:
                    temp.next = None
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

    def search(self, object):
        temp = self.head
        index = 0
        while temp.next is not None and temp.frequency != object:
            temp = temp.next
            index += 1
        else:
            if temp.frequency == object:
                return index
            else:
                return None


list = LinkedList()
list.add(4, 1)
list.add(5, 2)
list.add(3, 3)
list.add("X", 10)
list.add("E", 0)
list.add("V", 0)
list.add("O", 0)
list.add("L", 0)
list.remove(4)
list.print()

index = list.search(3)
element = list.getElement(index)
print(element.frequency)
print(element.next.frequency)
