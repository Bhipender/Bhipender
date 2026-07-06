# 4.Count and display the total number of nodes in the linked list.

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

    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

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

linklist1.display()

print("Total nodes =", linklist1.count_nodes())