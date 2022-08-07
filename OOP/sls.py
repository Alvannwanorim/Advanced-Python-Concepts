class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(seld,value):
        newNode = Node(value)
        return newNode

sls = SinglyLinkedList()
print(sls.push(1))