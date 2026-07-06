# 9.Create a queue and insert the values 10, 20, 30, 40.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Queue:")
queue.display()