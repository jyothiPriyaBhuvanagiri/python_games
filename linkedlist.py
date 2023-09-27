class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
print(node1)


class LinkedList:
    def __init__(self):
        self.head = None

    def IsLinkedListEmpty(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " ", end="")
                n = n.next

    def addingNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def addMiddle(self, data, prev, nxt):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = new_node
            prev.next = temp
            temp.next = nxt

    def addAfter(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("empty list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


list = LinkedList()
list.addingNode(10)
list.addingNode(20)
list.addingNode(30)
list.addEnd(50)
list.addEnd(15)
list.addAfter(12, 10)

list.IsLinkedListEmpty()
