# 2.Insert a new node containing 25 after the node containing 20.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after(self, key, data):
        temp = self.head

        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("Node not found")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


linklist1 = LinkedList()

linklist1.insert(10)
linklist1.insert(20)
linklist1.insert(30)
linklist1.insert(40)
linklist1.insert(50)

linklist1.insert_after(20, 25)

linklist1.display()