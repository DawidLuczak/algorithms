from Lists import PriorityQueue


class Node:
    frequency = 0
    right, left = None, None
    character = ""

    def isLeaf(self):
        return self.character != ""

    def __init__(self, value, char):
        self.character = char
        self.frequency = value

    def __lt__(self, other):
        if isinstance(other, Node):
            if self.frequency != other.frequency:
                return self.frequency < other.frequency
            if not self.isLeaf() and other.isLeaf():
                return True
            if self.isLeaf() and not other.isLeaf():
                return False
            if self.isLeaf() and other.isLeaf:
                return ord(self.character[0]) > ord(other.character[0])
            return True

    def __str__(self):
        return f'[{self.character} : {self.frequency}]'

    def __repr__(self):
        return f'[{self.character} : {self.frequency}]'


class HuffmanCode:
    text: str
    key: str
    rootNode: Node

    def __init__(self, text, key):
        self.text = text
        self.text = self.text.lower()
        self.key = key
        self.rootNode = self.createTree(self.text)

    def createTree(self, text):
        occurrences = {}
        for char in text:
            if occurrences.__contains__(char):
                occurrences[char] += 1
            else:
                occurrences[char] = 1
        nodes = PriorityQueue.PriorityQueue(len(occurrences) * 2)
        for char in occurrences.keys():
            node = Node(occurrences[char], char)
            nodes.enqueue(node)
        while not nodes.isEmpty():
            node1: Node = nodes.dequeue()
            node2: Node = nodes.dequeue()
            if isinstance(node2, Node):
                if node1.frequency == node2.frequency:
                    node1, node2 = node2, node1
                parent = Node(node1.frequency + node2.frequency, "")
                parent.left = node1
                parent.right = node2
                rootNode = parent
                nodes.enqueue(parent)
        return rootNode

    def encrypt(self, text, key, node):
        if node is None:
            return text
        if node.isLeaf():
            print(node.character + " : " + key)
            text = text.replace(node.character, key)
        text = self.encrypt(text, key + "0", node.left)
        text = self.encrypt(text, key + "1", node.right)
        return text

    def decrypt(self, text, rootNode):
        decoded = ""
        currentNode = rootNode
        for char in text:
            if char == '0':
                if currentNode.left.isLeaf():
                    decoded += currentNode.left.character
                    currentNode = rootNode
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right.isLeaf():
                    decoded += currentNode.right.character
                    currentNode = rootNode
                else:
                    currentNode = currentNode.right
        return decoded

    def print(self, rootnode):
        node = rootnode
        print(node)
        if node.left is not None:
            self.print(node.left)
        if node.right is not None:
            self.print(node.right)


tree = HuffmanCode("Magic Fungus", "")
code = tree.encrypt(tree.text, tree.key, tree.rootNode)
message = tree.decrypt(code, tree.rootNode)
print(code)
print(message)